# from src.connection import get_connection


# def list_all_events():
#     conn = get_connection()

#     with conn.cursor() as cursor:

#         get_all_events = """
#                         SELECT *
#                         FROM events
#                         """
        
#         cursor.execute(get_all_events)
#         events = cursor.fetchall()
#         conn.commit()

#     return cursor
