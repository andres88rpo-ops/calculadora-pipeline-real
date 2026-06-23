import os
from flask import Flask, render_template_string, send_file

app = Flask(__name__)

# 1. Ruta para descargar la versión Clásica
@app.route('/descargar_classic')
def descargar_classic():
    ruta = "Calculadora_Classic.zip"
    if os.path.exists(ruta):
        return send_file(ruta, as_attachment=True)
    return "Error: El archivo de la versión clásica no está disponible.", 404

# 2. Ruta para descargar la versión PRO
@app.route('/descargar_pro')
def descargar_pro():
    ruta = "Calculadora_PRO.zip"
    if os.path.exists(ruta):
        return send_file(ruta, as_attachment=True)
    return "Error: El archivo de la versión PRO no está disponible.", 404

# 3. Servidor de la interfaz gráfica (Versión BLUE inicial)
@app.route('/')
def home():
    # Variable de entorno administrada para identificar el ambiente
    ambiente = os.environ.get('APP_ENV', 'Desarrollo Local')
    
    html_blue = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Portal de Descargas - Ambiente BLUE</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; text-align: center; padding-top: 50px; }}
            .card {{ background: white; max-width: 500px; margin: 0 auto; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-top: 5px solid #0066cc; }}
            h1 {{ color: #333; }}
            h2 {{ color: #0066cc; }}
            .btn {{ display: inline-block; padding: 12px 20px; background-color: #0066cc; color: white; text-decoration: none; border-radius: 5px; margin: 10px; font-weight: bold; }}
            .btn:hover {{ background-color: #004499; }}
            .btn-alt {{ background-color: #555; }}
            .btn-alt:hover {{ background-color: #333; }}
            .footer {{ margin-top: 20px; color: #777; font-size: 0.9em; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Calculadora Tech</h1>
            <h2>Ambiente Producción (BLUE)</h2>
            <p>Versión actual del sistema: <strong>v1.0.0 (Interfaz Clásica)</strong></p>
            <br>
            <a href="/descargar_classic" class="btn">Descargar Calculadora Clásica (V1)</a>
            <a href="/descargar_pro" class="btn btn-alt">Descargar Calculadora PRO (V2)</a>
            
            <div class="footer">
                <p>Variable de Entorno: APP_ENV = {ambiente}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_blue)

if __name__ == '__main__':
    # Localmente correrá en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)