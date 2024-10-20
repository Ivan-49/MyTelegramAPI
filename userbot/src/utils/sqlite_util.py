import sqlite3


class DataBase(): 
    def __init__(self, path) -> None:
        self.path = path # путь к БД
        self.db = sqlite3.connect(self.path) #
        self.cursor = self.db.cursor()
        self.db.commit()#


    """
    метод для создания новой таблицы принимает название таблицы и словарь с именами столбцов и их типами данных  
    
    """
    def create_table(self, table_title:str, column_names_and_data_types:dict):
        column = [i for i in column_names_and_data_types.items()]
        for i ,val in enumerate(column):
            column[i] = list(val)
        for i in column:
            if i[1] == 'int':
                i[1] = 'integer'
            if i[1] == 'str':
                i[1] = 'text'
        all_column = ''
        for i ,val in enumerate(column):
            all_column = all_column + ' '.join(val) + ','
        self.cursor.execute(f"""
                            CREATE TABLE {table_title} (
                                {all_column.rstrip(',')}
                            )
                            """)


    '''
    функция для того что бы вытянуть данные из таблицы, принимает название таблицы как обязательный аргумент 
    и услевие и название столбцов как не обязательные возвращает все данных которые подходили условиям 
    '''
    def get_data(self, table_title:str = '', where:str = '', column_title:str = '*'):
        if where:
            where = "WHERE " + where
        self.cursor.execute(f""" SELECT {column_title} 
                            FROM {table_title} 
                            {where}
                            """)
        return self.cursor.fetchall()


    '''
    функиця для получения данных о таблице и ее столбцах
    '''
    def get_table_column_info(self, table_title:str = '', full_info:bool = False):
        self.cursor.execute(f"""
                            PRAGMA table_info({table_title})
                            """)
        all_info = self.cursor.fetchall()
        info = []
        if full_info:
            return all_info
        else: 
            for i in all_info:
                info.append((i[0], i[1],i[2]))
    
        return tuple(info)
    

    '''
    функция для добавления данных в таблицу принимает название табицы и лист с данными
    '''
    def add_data(self, table_title:str = '', data:list = []):
        if data == []:
            return f'names column:{self.get_table_column_info(table_title=table_title)}'
        end = ''
        for i in data:
            if type(i) == str:
                end += f"'{i}', "
            if type(i) == int:
                end += f"{str(i)}, "
        end = end.rstrip(', ')
        self.cursor.execute(f"""
                            INSERT INTO {table_title} 
                            VALUES ({end})
                            """)
        self.db.commit()
        

    '''
    метод для удаления таблицы
    '''
    def delete_table(self, table_title:str = ''):
        self.cursor.execute(f"""
                            DROP TABLE {table_title} 
                            """)
        self.db.commit()
        
    

    '''
    метод для удаления данных из таблицы принимает название условие, так же имеет help для помощи 
    '''
    def delete_data(self, table_title:str = '', where:str = '', help = False):
        if help:
            return f'names column:{self.get_table_column_info(table_title=table_title)}'        
        self.cursor.execute(f"""
                            DELETE FROM {table_title} WHERE {where}
                            """)
        self.db.commit()
    

    '''
    меторд для обновления данных в таблице принимает название таблицы название колонок условие и данные
    '''
    def update_data(self, table_title:str = '', column_name:str = '*', where:str = '',data: str = '0'):

        self.cursor.execute(f"""
                            UPDATE {table_title}
                            SET {column_name} = {data} 
                            WHERE {where}
                            """)
        self.db.commit()
    
    '''
    метод для получения кол-ва элементов/строк в таблице
    '''
    def get_number_of_objects(self, table_title:str):
        self.cursor.execute(f"select count(*) from {table_title}")
        return(int(self.cursor.fetchall()[0][0]))
    