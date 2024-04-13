# Проверяем дз раскомитивая "from"

from app_task_1 import app      # Заходим по /students/
#from app_task_2 import app      # Заходить по /books/
#from app_task_3 import app      # Заходить по /scores/
#from app_task4 import app        # Заходим по /register/

if __name__ == '__main__':
    app.run(debug=True)