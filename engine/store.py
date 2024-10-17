from engine.core import ThreadSafeSingletonMeta
from abc import ABC, abstractmethod
from typing import (
    Self,
    Dict,
    List,
    Callable
)

class StoreComponent(ABC):

    """
    Declare common operation for all the nodes it the tree.
    """
    _parent = None
    _name = None
    _setters = {}
    _getters = {}

    @property
    def parent(cls) -> Self:
        return cls._parent

    @parent.setter
    def parent(cls, parent: Self):
        cls._parent = parent
        cls._name = f"{cls._parent.id}/{cls.id}"

    @parent.getter
    def parent(cls) -> Self:
        return cls._parent

    @property
    def id(cls) -> str:
        return cls.id

    @id.setter
    def id(cls, name: str) -> None:
        # Ensure the name is unique and is a path like.
        # Allowing to target a node like <root_name>/<node_name>/.../target
        if cls._parent != None:
            cls._name = f"{cls._parent.id}/{name}"
        else:
            cls._name = name


    @id.getter
    def id(cls) -> str:
        return cls._name


    """
    It's easier to have the child managment here. Even if it will lead to empty
    functions for leaves.
    """

    def add(cls, component: Self) -> None:
        pass

    def remove(cls, component: Self) -> None:
        pass

    def is_composite(cls) -> bool:
        return False

    """
    Store getter and setter
    """
    @property
    def setters(cls) -> List[Callable]:
        return cls._setters

    @setters.setter
    def setters(cls, setters: Dict):
        cls._setters = setters

    @setters.getter
    def setters(cls) -> List[Callable[[str, List[str]], Callable]]:
        return cls._setters

    @property
    def getters(cls) -> List[Callable]:
        return cls._getters

    @getters.setter
    def getters(cls, getters: Dict):
        cls._getters = getters

    @getters.getter
    def getters(cls) -> List[Callable[[str, List[str]], Callable]]:
        return cls._getters


    def get_setter(cls, setter_name):
        return cls._setters[setter_name]

    def add_setter(cls, setter):
        cls._setters[setter.__name__] = setter

    def get_setters(cls, target: str, attributes: List[str]):
        if target == cls.id:
            return list(map(lambda attr_name: cls._setters[attr_name], attributes))
        else:
            return []


    def get_getter(cls, getter_name):
        return cls._getters[getter_name]

    def add_getters(cls, getter):
        cls._getters[getter.__name__] = getter

    def get_getters(cls, target: str, attributes: List[str]):
        if target == cls.id:
            return list(map(lambda attr_name: cls._getters[attr_name], attributes))
        else:
            return []


    @abstractmethod
    def map_setters(cls, target: str, attributes: List[str]):
        pass

    @abstractmethod
    def map_getters(cls, target: str, attributes: List[str]):
        pass

    @abstractmethod
    def add_node(cls, target: str, node: Self):
        pass

    @abstractmethod
    def get_child_map(cls) -> str:
        pass


class StoreComposite(StoreComponent):
    """
    Intermediate tree node. Can have childs.
    """

    def __init__(cls) -> None:
        cls._children: Dict[str:Self] = {}

    def add(cls, component: StoreComponent) -> None:
        cls._children[component.id] = component
        component.parent = cls

    def remove(cls, component: StoreComponent) -> None:
        try:
            del cls._children[component.id]
        except:
            pass
        component.parent = None

    def is_composite(cls) -> bool:
        return True

    """
    Traverses recursively through all children collecting setters matching the
    attributes list if the child name is equal to the target
    """
    def map_setters(cls, target: str, attributes: List[str]):
        setters = cls.get_setters(target, attributes)
        for child in cls._children.values():
            setters.extend(child.map_setters(target, attributes))
        return setters

    """
    Traverses recursively through all children collecting getters matching the
    attributes list if the child name is equal to the target
    """
    def map_getters(cls, target: str, attributes: List[str]):
        getters = cls.get_getters(target, attributes)
        for child in cls._children:
            getters.extend(child.map_getters(target, attributes))
        return getters

    def add_node(cls, target: str, node: StoreComponent):
        if target == cls._name:
            cls.add(node)
        else:
            for child in cls._children.values():
                child.add_node(target, node)

    def get_child_map(cls) -> str:
        map = f"\n- {cls.id}"
        for child in cls._children.values():
            map += f"  {child.get_child_map()}\n"
        return map

class EngineStore(metaclass=ThreadSafeSingletonMeta):
    _data: StoreComponent

    def __init__(cls) -> None:
        data_root = StoreComposite()
        data_root.id = "root"
        cls._data = data_root

    def get_component_setter(cls, target: str, setters: List[str]):
        cls._data.map_setters(target, setters)

    def get_component_getter(cls, target: str, getters: List[str]):
        cls._data.map_setters(target, getters)

    def add_node(cls, target: str, node: StoreComponent):
        cls._data.add_node(target, node)

    def get_map(cls):
        print(vars(cls._data))
        return cls._data.get_child_map()

    # queries
    def had_player(cls) -> bool:
        player_exist = cls.get_component_getter("player", ['exist'])