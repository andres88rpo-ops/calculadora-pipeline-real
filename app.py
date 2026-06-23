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

# 3. Servidor de la interfaz gráfica (Versión GREEN modificada)
@app.route('/')
def home():
    # Variable de entorno administrada para identificar el ambiente
    ambiente = os.environ.get('APP_ENV', 'Desarrollo Local')
    
    html_green = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Portal de Descargas - Ambiente GREEN</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #121214; text-align: center; padding-top: 50px; color: #e1e1e6; }}
            .card {{ background: #202024; max-width: 500px; margin: 0 auto; padding: 30px; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.4); border-top: 5px solid #00b37e; }}
            h1 {{ color: #ffffff; }}
            h2 {{ color: #00b37e; }}
            p {{ color: #a8a8b3; }}
            .btn-pro {{ display: inline-block; padding: 12px 25px; background-color: #00b37e; color: white; text-decoration: none; border-radius: 5px; margin: 10px; font-weight: bold; font-size: 1.1em; box-shadow: 0 4px 12px rgba(0, 179, 126, 0.3); transition: background 0.2s; }}
            .btn-pro:hover {{ background-color: #00875f; }}
            .btn-classic {{ display: inline-block; padding: 10px 18px; background-color: #4d4d57; color: #e1e1e6; text-decoration: none; border-radius: 5px; margin: 10px; font-size: 0.9em; transition: background 0.2s; }}
            .btn-classic:hover {{ background-color: #3c3c42; }}
            .footer {{ margin-top: 30px; color: #7c7c8a; font-size: 0.85em; border-top: 1px solid #29292e; padding-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Calculadora Tech Pro</h1>
            <h2>Ambiente Staging (GREEN)</h2>
            <p>¡Actualización completada con éxito!</p>
            <p>Versión actual del sistema: <strong>v2.0.0 (Interfaz Moderna)</strong></p>
            <br>
            
            <a href="/descargar_pro" class="btn-pro">🚀 Descargar Nueva Calculadora PRO (V2)</a>
            <br>
            <a href="/descargar_classic" class="btn-classic">Descargar Versión Clásica Anterior (V1)</a>
            
            <div class="footer">
                <p>Variable de Entorno: APP_ENV = {ambiente}</p>
                <p>&copy; 2026 - Control de Versiones con Despliegue Avanzado</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_green)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
