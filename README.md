# Dragon Ball Z - Explorer

> This projet is made during for school purpose. All right reserved to the promotion 24/25 B3 DEV Ecole CCI.

## How to run

This is a standalone python script.

```bash
git pull https://github.com/nak0x/dbz-explorer.git
cd ./dbz-explorer
python3 ./main.py
```

## Structure
The project is structured by folder responsabilty name

### The game engine:

The Engine is composed off a scene manager, a store and his responsabilty is to maintain the game loop.

The scene manager is a state manager, that keep in memory the current scene and allow the engine to execute per scene logiques.

The store is a composite tree that store the game data, and expose "easy" to query data.
(Probably the worst choice of this project...)

The game engine embed an Input system with an Observer patter to notify the InputHandler that
a valid input as being done and that he can return this input to where it has being called.

### The game:

The game work around the Caracter facade. In the idea it's a pokemon like game, where the player train his character, and fight some other to capture theme.

The Character is a just a simple object, but it is controlled by the a Factory to contruct them.
The factory use a Builder to easily build a character.
There is a state management inside the charcter to control his transformations.

All the objects in the game, inculding items, techniques and transformation that the player accumulate are store by an Inventory and are children of the Item class that define how the invertory can interact with them.
An item have a `use` function that take a character target and apply specific effect.

See more in `./characters/_inventory/items`