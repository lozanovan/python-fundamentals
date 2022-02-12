import keyboard,json,random,psycopg2
from faker import Faker

class ETL:

    data = []
    data_sink=""

    def source(self, data_source: str):
        if data_source == 'Simulation':
            self.generate_random_json()            
            
        elif data_source == 'File':          
            self.read_json_file()
        return self

    def sink(self, data_sink: str):
        self.data_sink = data_sink
        return self

    def run(self):
        if self.data_sink == 'Console':
            self.print_data(self.data)          

        elif self.data_sink == 'PostgreSQL':
            self.populate_db()                

    def generate_random_json(self):
        fake = Faker('en_US')
        print("Please enter 'y' for generating number of json objects and 'n' to stop.")
        while True:
            if keyboard.read_key() == "y":    
                my_dict = { 'Name': fake.name(), 'Score': float(random.randrange(155, 389))/100   }

                self.data.append(my_dict)
                #print(my_dict)
            elif keyboard.read_key() == "n":
                break
        return self
            
    def read_json_file(self):
        with open("sample.json", "r") as f:
            row_data = json.load(f)

            for i in row_data:
                self.data.append(i)
                #print(i)
        f.close()
        return self

    def print_data(self, data):
        print(json.dumps(data, indent = 1))

    def populate_db(self):
        try:
            conn = psycopg2.connect(user="postgres",
                                        password="postgre",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="etl")
            cur = conn.cursor()

            cur.execute("CREATE TABLE IF NOT EXISTS t_results (Row_ID INT GENERATED ALWAYS AS IDENTITY, Name VARCHAR(100), Score NUMERIC(2));")

            #iterate each json entity and insert it into the db
            for item in self.data:
                cur.execute(f"INSERT INTO t_results (Name, Score) VALUES ('{item['Name']}', {item['Score']});")
            
            conn.commit()
            conn.close()
            print("Json data inserted successfuly into PostgreSQL db.")

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
        
#ETL().source('Simulation').sink('PostgreSQL').run()
#ETL().source('Simulation').sink('Console').run()
#ETL().source('File').sink('Console').run()
ETL().source('File').sink('PostgreSQL').run()


