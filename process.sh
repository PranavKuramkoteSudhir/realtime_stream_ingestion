source venv/bin/activate
python config.py
docker compose up -d
#check for running containers
docker ps


# install requirements
pip install -r requirements.txt

# create postgres database
docker exec -i postgres psql -U user -d mydb < ./db_conf/DB_init.sql
# add seed data to postgres
python db_conf/seed.py

mkdir jars
mkdir config

#make the file runnable
chmod +x plugins.sh
#run the file
./plugins.sh

#create kafka topics
docker exec -it broker kafka-topics \
  --create --topic clicks \
  --partitions 3 --replication-factor 1 \
  --bootstrap-server broker:29092

docker exec -it broker kafka-topics \
  --create --topic checkouts \
  --partitions 3 --replication-factor 1 \
  --bootstrap-server broker:29092

  

# check connectors 
docker exec -it flink-jobmanager ls /opt/flink/lib

# run job embedding and run
docker exec -it flink-jobmanager ./bin/sql-client.sh embedded -f /opt/flink/sql/enrich.sql

#run producer
python producer/data_source.py

# restart jobmanager and taskmanager to pick up new jars
docker compose restart jobmanager taskmanager


#flink sql client
docker exec -it flink-jobmanager ./bin/sql-client.sh

#list topics
docker exec -it broker kafka-topics --list --bootstrap-server broker:29092



