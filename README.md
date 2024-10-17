# Dragon Ball Z - Explorer

> This projet is made during for school purpose. All right reserved to the promotion 24/25 B3 DEV Ecole CCI.

## Specs

> [link](https://designpattern.nexelab.com/c/21-tp/)

In this game the goal is to collect as much as character as possible.
It's a pokemon like, but in the dbz univers.

## Classes

### Engine([[#EngineMeta]])
The game engine is a singleton facade in charge of the game runtime.
#### Construct
- state: [[#EngineState]]
- store: [[#EngineStore]]
- renderer: [[#EngineRederer]]
- input_handler: [[#InputHandler]]
#### Methods
- ##### run()
  Start the runtime. 
  
### EngineMeta
Thread-safe implementation of Singleton. Describe the behavior when instantiate.

### EngineState
The `EngineState` is the context of the [[#Engine( EngineMeta )]] state.
#### Construct
- state: [[#State]]
#### Methods
- ##### mutate(state: [[#State]])
  Change the state to the provided one.
- ##### get_state() -> [[#EngineStateEnum]]
  Return the current state name
### State
The base state interface
#### Property
- ##### context(context:[[#EngineState]])
  Set the context of the state
#### Methods
- ##### create_player()
- ##### train_character()
- ##### fight_character()
- ##### manage_character()

### EngineStore

The `EngineStore` is in charge of being a single point of true for the game general data.
Such as 

- Items: All the available items
- Charaters: All the character the player manager to collect
- Fights: All the fight the player engage.


x