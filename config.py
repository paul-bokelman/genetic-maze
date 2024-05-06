# all config 

sim_config = {
    "cell_size": 40,
    "padding": 10,
    "evo_delay": 100,
    "maze": {
        "start": {"char": "s", "color": "#32a852"},
        "end": {"char": "e", "color": "#8a42f5"},
        "open": {"char": "o", "color": "#fff"},
        "closed": {"char": "c", "color": "#000"},
    }
}

builder_species_config = {
    "maze_size":  8,
    "n_organisms": 50,
    "tournament_proportion": 0.8, 
    "mutation_probability": 0.5,  
}

solver_species_config = {

}