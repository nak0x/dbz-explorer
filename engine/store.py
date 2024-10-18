from engine.core import ThreadSafeSingletonMeta
from abc import ABC, abstractmethod
from typing import (
    Self,
    Dict,
    List,
    Callable,
    Any
)

class StoreComponent(ABC):

    """
    Declare common operation for all the nodes it the tree.
    """
    _data: Any
    _parent = None
    _id = None
    _setters = {}
    _getters = {}

    @property
    def parent(self) -> Self:
        return self._parent

    @parent.setter
    def parent(self, parent: Self):
        self._parent = parent
        self._id = f"{self._parent.id}/{self.id}"

    @parent.getter
    def parent(self) -> Self:
        return self._parent

    @property
    def id(self) -> str:
        return self.id

    @id.setter
    def id(self, id: str) -> None:
        # Ensure the name is unique and is a path like.
        # Allowing to target a node like <root_name>/<node_name>/.../target
        if self._parent != None:
            self._id = f"{self._parent.id}/{id}"
        else:
            self._id = id


    @id.getter
    def id(self) -> str:
        return self._id


    """
    It's easier to have the child managment here. Even if it will lead to empty
    functions for leaves.
    """

    def add(self, component: Self) -> None:
        pass

    def remove(self, component: Self) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    """
    Store getter and setter
    """
    @property
    def setters(self) -> List[Callable]:
        return self._setters

    @setters.setter
    def setters(self, setters: Dict):
        self._setters = setters

    @setters.getter
    def setters(self) -> List[Callable[[str, List[str]], Callable]]:
        return self._setters

    @property
    def getters(self) -> List[Callable]:
        return self._getters

    @getters.setter
    def getters(self, getters: Dict):
        self._getters = getters

    @getters.getter
    def getters(self) -> List[Callable[[str, List[str]], Callable]]:
        return self._getters


    def get_setter(self, setter_name):
        try:
            return self._setters[setter_name]
        except:
            raise Exception(f"Undefined setter for {self._id}: {setter_name}")

    def add_setter(self, setter: Callable):
        self._setters[setter.__name__] = setter

    def get_setters(self, target: str, attributes: List[str]):
        if target == self._id:
            return list(map(lambda attr_name: self.get_setter(attr_name), attributes))
        else:
            return []


    def get_getter(self, getter_name):
        try:
            return self._getters[getter_name]
        except:
            raise Exception(f"Undefined getter for {self._id}: {getter_name}")

    def add_getter(self, getter: Callable):
        self._getters[getter.__name__] = getter

    def get_getters(self, target: str, attributes: List[str]):
        if target == self._id:
            return list(map(lambda attr_name: self.get_getter(attr_name), attributes))
        else:
            return []


    @abstractmethod
    def map_setters(self, target: str, attributes: List[str]):
        pass

    @abstractmethod
    def map_getters(self, target: str, attributes: List[str]):
        pass

    @abstractmethod
    def add_node(self, target: str, node: Self):
        pass

    @abstractmethod
    def get_child_map(self) -> str:
        pass

    @abstractmethod
    def had_child(self) -> bool:
        pass


class StoreComposite(StoreComponent):
    """
    Intermediate tree node. Can have childs.
    """

    def __init__(self, name) -> None:
        self._children: Dict[str:Self] = {}
        self.add_getter(self.exist)
        self.id = name

    def add(self, component: StoreComponent) -> None:
        self._children[component.id] = component
        component.parent = self

    def remove(self, component: StoreComponent) -> None:
        try:
            del self._children[component.id]
        except:
            pass
        component.parent = None

    def exist(self) -> bool:
        return True

    def had_child(self) -> bool:
        if len(self._children) > 0:
            return True
        return False

    """
    Traverses recursively through all children collecting setters matching the
    attributes list if the child name is equal to the target
    """
    def map_setters(self, target: str, attributes: List[str]):
        setters = self.get_setters(target, attributes)
        for child in self._children.values():
            setters.extend(child.map_setters(target, attributes))
        return setters

    """
    Traverses recursively through all children collecting getters matching the
    attributes list if the child name is equal to the target
    """
    def map_getters(self, target: str, attributes: List[str]):
        getters = self.get_getters(target, attributes)
        for child in self._children.values():
            getters.extend(child.map_getters(target, attributes))
        return getters

    def add_node(self, target: str, node: StoreComponent):
        if target == self._id:
            self.add(node)
        else:
            for child in self._children.values():
                child.add_node(target, node)

    def get_child_map(self) -> str:
        map = f"\n- {self.id}"
        for child in self._children.values():
            map += f"  {child.get_child_map()}\n"
        return map

class EngineStore(metaclass=ThreadSafeSingletonMeta):
    _data: StoreComponent

    def __init__(self) -> None:
        data_root = StoreComposite("root")
        self._data = data_root

    def get_component_setter(self, target: str, setters: List[str]):
        return self._data.map_setters(target, setters)

    def get_component_getter(self, target: str, getters: List[str]):
        return self._data.map_getters(target, getters)

    def add_node(self, target: str, node: StoreComponent):
        self._data.add_node(target, node)

    def get_map(self):
        print(vars(self._data))
        return self._data.get_child_map()

    # queries
    def had_player(self) -> bool:
        player_exist = self.get_component_getter("player", ['exist'])