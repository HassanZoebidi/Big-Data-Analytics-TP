docker compose exec spark-master /opt/spark/bin/spark-submit --class spark.streaming.tp22.Stream --master spark://spark-master:7077 /workspace/streaming/target/stream-1.0-SNAPSHOT.jar rate 5


