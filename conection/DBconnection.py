import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def get_supabase_client() -> Client:
    """
    Obtiene el cliente de Supabase configurado
    
    Returns:
        Client: Cliente de Supabase listo para usar
    """
    # Obtener credenciales
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL y SUPABASE_KEY deben estar definidas en el archivo .env")
    
    # Crear y retornar cliente
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase

def verificar_conexion():
    """Función simple para verificar conexión a Supabase"""
    try:
        supabase = get_supabase_client()
        # Probar conexión
        response = supabase.table("users").select("id").limit(1).execute()
        print("✅ Conexión exitosa a Supabase!")
        return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

if __name__ == "__main__":
    verificar_conexion()