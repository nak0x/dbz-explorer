from engine.engine import (
    Engine,
    EngineStore,
    EngineState,
    InputHandler
)

from engine.state import CreatingCharacterState

initial_state = CreatingCharacterState()

game_state = EngineState(initial_state)
game_store = EngineStore()
game_input_handler = InputHandler()
game_engine = Engine(
    store=game_store,
    state=game_state,
    input_handler=game_input_handler
)

game_engine.run()