from day25.estd_connection import estd_connection


def delete(student_id):
    cursor = estd_connection()
    sql = f"""
    DELETE FROM STUDENT WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    print("Student deleted successfully !!")
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False
