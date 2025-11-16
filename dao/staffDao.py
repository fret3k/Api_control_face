from conection.supabaseClient import supabase

class StaffDAO:

    @staticmethod
    def get_all():
        return supabase.table("staff").select("*").execute()

    @staticmethod
    def get_by_id(staff_id: int):
        return supabase.table("staff").select("*").eq("id", staff_id).single().execute()

    @staticmethod
    def create(data: dict):
        return supabase.table("staff").insert(data).execute()

    @staticmethod
    def update(staff_id: int, data: dict):
        return supabase.table("staff").update(data).eq("id", staff_id).execute()

    @staticmethod
    def delete(staff_id: int):
        return supabase.table("staff").delete().eq("id", staff_id).execute()
