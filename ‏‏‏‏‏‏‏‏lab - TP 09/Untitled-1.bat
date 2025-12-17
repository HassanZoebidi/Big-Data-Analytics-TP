docker compose exec spark-master rm -rf /workspace/wordcount-spark/target/out-docker
docker compose exec spark-master /opt/spark/bin/spark-submit --class spark.batch.tp21.WordCountTask --master spark://spark-master:7077 /workspace/wordcount-spark/target/wordcount-spark-1.0-SNAPSHOT.jar /workspace/wordcount-spark/src/main/resources/loremipsum.txt /workspace/wordcount-spark/target/out-docker

docker compose exec nc sh -c "apk add --no-cache netcat-openbsd >/dev/null && nc -lk -p 9999"


docker compose exec spark-master /opt/spark/bin/spark-submit ^
  --class spark.streaming.tp22.Stream ^
  --master spark://spark-master:7077 ^
  /workspace/streaming/target/stream-1.0-SNAPSHOT.jar
