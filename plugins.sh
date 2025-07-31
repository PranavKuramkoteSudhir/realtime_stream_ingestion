#!/bin/bash

set -e

mkdir -p jars
cd jars

download_jar() {
    local url=$1
    local filename=$2
    
    if [ -f "$filename" ]; then
        echo "$filename already exists"
    else
        echo "Downloading $filename..."
        curl -L -o "$filename" "$url"
    fi
}

download_jar "https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka/3.1.0-1.17/flink-connector-kafka-3.1.0-1.17.jar" "flink-connector-kafka-3.1.0-1.17.jar"
download_jar "https://repo1.maven.org/maven2/org/apache/flink/flink-connector-jdbc/3.1.1-1.17/flink-connector-jdbc-3.1.1-1.17.jar" "flink-connector-jdbc-3.1.1-1.17.jar"
download_jar "https://repo1.maven.org/maven2/com/alibaba/ververica/flink-connector-elasticsearch8/1.17-vvr-8.0.11-4/flink-connector-elasticsearch8-1.17-vvr-8.0.11-4.jar" "flink-connector-elasticsearch8-1.17-vvr-8.0.11-4.1.jar"
download_jar "https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.4.0/kafka-clients-3.4.0.jar" "kafka-clients-3.4.0.jar"
download_jar "https://repo1.maven.org/maven2/org/postgresql/postgresql/42.6.0/postgresql-42.6.0.jar" "postgresql-42.6.0.jar"