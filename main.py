import re, json, hashlib, time
from typing import Dict, Tuple

##
## Generate a unique id for the graph
##
def gen_graph_id() -> str:
    return hashlib.sha512(str(time.time()).encode('utf-8')).hexdigest()

    ##
    ## End of function
    ##

##
## Calculate the euclidean distance
##
def euc_dist(a: Tuple, b: Tuple) -> float:
    x1, y1 = a
    x2, y2 = b

    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    ##
    ## End of function
    ##

##
## Parse a tsp file function
##
def parse_euc_2d_tsp_file(file_path: str) -> Dict[str, Dict]:
    """Convert a .tsp file intom a json graph file

    Args:
        file_path (str): the path to the .tsp file

    Returns:
        Dict[str, Dict]: None
    """
    with open(file_path, "r") as file:
        lines = file.read().split("NODE_COORD_SECTION")[1].split("EOF")[0].split("\n")
        lines = [line for line in lines if line.strip()]

    graph_id = gen_graph_id()
    graph = {
        graph_id: {
            "id": graph_id,
            "nodes": [],
            "edges": [],
            "adj_matrix": [],
            "shortest_tour": None
        }
    }

    ##
    ## Store the nodes in the graph
    ##
    for line in lines:
        idx, x, y = re.split(r"\s+", line.strip())

        ## Append the node
        graph[graph_id]["nodes"].append({
            "idx": int(idx),
            "x": float(x),
            "y": float(y)
        })

        ## Update the adjacency matrix


    ##
    ## Calculate the edges.
    ##
    edge_idx = 0

    for node in graph[graph_id]["nodes"]:
        for other_node in graph[graph_id]["nodes"]:
            if node == other_node:
                continue
              
            weight = euc_dist(
                (node["x"], node["y"]), (other_node["x"], other_node["y"]))

            graph[graph_id]["edges"].append({
                "idx": edge_idx,
                "weight": weight,
                  "start": node,
                  "end": other_node
            })
    
    ##
    ## Return the new dictionary with all of the tsp data
    ##
    return graph

    ##
    ## End of function
    ##

##
## Main function
##
def main():
    euc_2d_tsp_files = [
      "a280.tsp",    # 280 nodes, distance: 2579
      "berlin52.tsp",    # 52 nodes, distance: 7542
      "bier127.tsp",    # 127 nodes, distance: 118282
      "brd14051.tsp",    # 14051 nodes, distance: [468942, 469445]
      "ch130.tsp",    # 130 nodes, distance: 6110
      "ch150.tsp",    # 150 nodes, distance: 6528
      "d198.tsp",    # 198 nodes, distance: 15780
      "d493.tsp",    # 493 nodes, distance: 35002
      "d657.tsp",    # 657 nodes, distance: 48912
      "d1291.tsp",    # 1291 nodes, distance: 50801
      "d1655.tsp",    # 1655 nodes, distance: 62128
      "d2103.tsp",    # 2103 nodes, distance: [79952, 80450]
      "d15112.tsp",    # 15112 nodes, distance: [1564590, 1573152]
      "d18512.tsp",    # 18512 nodes, distance: [644650, 645488]
      "eil51.tsp",    # 51 nodes, distance: 426
      "eil76.tsp",    # 76 nodes, distance: 538
      "eil101.tsp",    # 101 nodes, distance: 629
      "fl417.tsp",    # 417 nodes, distance: 11861
      "fl1400.tsp",    # 1400 nodes, distance: 20127
      "fl1577.tsp",    # 1577 nodes, distance: [22204, 22249]
      "fl3795.tsp",    # 3795 nodes, distance: [28723, 28772]
      "fnl4461.tsp",    # 4461 nodes, distance: 182566
      "gil262.tsp",    # 262 nodes, distance: 2378
      "kroA100.tsp",    # 100 nodes, distance: 21282
      "kroB100.tsp",    # 100 nodes, distance: 22141
      "kroC100.tsp",    # 100 nodes, distance: 20749
      "kroD100.tsp",    # 100 nodes, distance: 21294
      "kroE100.tsp",    # 100 nodes, distance: 22068
      "kroA150.tsp",    # 150 nodes, distance: 26524
      "kroB150.tsp",    # 150 nodes, distance: 26130
      "kroA200.tsp",    # 200 nodes, distance: 29368
      "kroB200.tsp",    # 200 nodes, distance: 29437
      "lin105.tsp",    # 105 nodes, distance: 14379
      "lin318.tsp",    # 318 nodes, distance: 42029
      "linhp318.tsp",    # 318 nodes, distance: 41345
      "nrw1379.tsp",    # 1379 nodes, distance: 56638
      "p654.tsp",    # 654 nodes, distance: 34643
      "pcb442.tsp",    # 442 nodes, distance: 50778
      "pcb1173.tsp",    # 1173 nodes, distance: 56892
      "pcb3038.tsp",    # 3038 nodes, distance: 137694
      "pr76.tsp",    # 76 nodes, distance: 108159
      "pr107.tsp",    # 107 nodes, distance: 44303
      "pr124.tsp",    # 124 nodes, distance: 59030
      "pr136.tsp",    # 136 nodes, distance: 96772
      "pr144.tsp",    # 144 nodes, distance: 58537
      "pr152.tsp",    # 152 nodes, distance: 73682
      "pr226.tsp",    # 226 nodes, distance: 80369
      "pr264.tsp",    # 264 nodes, distance: 49135
      "pr299.tsp",    # 299 nodes, distance: 48191
      "pr439.tsp",    # 439 nodes, distance: 107217
      "pr1002.tsp",    # 1002 nodes, distance: 259045
      "pr2392.tsp",    # 2392 nodes, distance: 378032
      "rat99.tsp",    # 99 nodes, distance: 1211
      "rat195.tsp",    # 195 nodes, distance: 2323
      "rat575.tsp",    # 575 nodes, distance: 6773
      "rat783.tsp",    # 783 nodes, distance: 8806
      "rd100.tsp",    # 100 nodes, distance: 7910
      "rd400.tsp",    # 400 nodes, distance: 15281
      "rl1304.tsp",    # 1304 nodes, distance: 252948
      "rl1323.tsp",    # 1323 nodes, distance: 270199
      "rl1889.tsp",    # 1889 nodes, distance: 316536
      "rl5915.tsp",    # 5915 nodes, distance: [565040, 565530]
      "rl5934.tsp",    # 5934 nodes, distance: [554070, 556045]
      "rl11849.tsp",    # 11849 nodes, distance: [920847, 923368]
      "st70.tsp",    # 70 nodes, distance: 675
      "ts225.tsp",    # 225 nodes, distance: 126643
      "tsp225.tsp",    # 225 nodes, distance: 3919
      "u159.tsp",    # 159 nodes, distance: 42080
      "u574.tsp",    # 574 nodes, distance: 36905
      "u724.tsp",    # 724 nodes, distance: 41910
      "u1060.tsp",    # 1060 nodes, distance: 224094
      "u1432.tsp",    # 1432 nodes, distance: 152970
      "u1817.tsp",    # 1817 nodes, distance: 57201
      "u2152.tsp",    # 2152 nodes, distance: 64253
      "u2319.tsp",    # 2319 nodes, distance: 234256
      "usa13509.tsp",    # 13509 nodes, distance: [19947008, 19982889]
      "vm1084.tsp",    # 1084 nodes, distance: 239297
      "vm1748.tsp",    # 1748 nodes, distance: 336556
  ]


    for file_path in euc_2d_tsp_files:
        print(f"generating graph for '{file_path}'")
        graph = parse_euc_2d_tsp_file("tsplib/" + file_path)

        with open("graphs/" + file_path + ".json", "w") as f:
            f.write(json.dumps(graph, indent=4))

    print("done")

    ##
    ## End of function
    ##

##
## Execute the code
##
if __name__ == "__main__":
    main()

##
## End of file
##