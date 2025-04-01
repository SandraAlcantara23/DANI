from flask import Flask, render_template, request
from puzzle import ejecutar_metodo  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = None

    if request.method == "POST":
        estado_inicial = list(map(int, request.form["estado_inicial"].split()))
        solucion = list(map(int, request.form["solucion"].split()))
        resultados = {}

        for metodo in ["BFS", "DFS", "DFS_recursivo"]:
            resultado = ejecutar_metodo(metodo, estado_inicial, solucion)
            resultados[metodo] = resultado  
        
        print(resultados)  
    
    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)