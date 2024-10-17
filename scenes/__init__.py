from enum import Enum
from typing import List

from engine.core.input_handler import Input, InputBuilder
from engine.scene import Scene
from engine.store import EngineStore

from enums import EngineSceneEnum

from scenes.home_scene import HomeScene
from scenes.creation_scene import CreationScene
from scenes.fight_scene import FightScene
from scenes.manage_scene import ManageScene
from scenes.train_scene import TrainScene
