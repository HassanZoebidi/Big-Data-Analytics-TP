package spark.streaming.tp22;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Encoders;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;
import org.apache.spark.sql.streaming.Trigger;

import java.util.Arrays;
import java.util.concurrent.TimeoutException;

public class Stream {
    public static void main(String[] args) throws StreamingQueryException, TimeoutException {
        // Mode selection:
        // - Default: socket on localhost:9999
        // - Custom socket: args[0]=host, args[1]=port
        // - Rate source: args[0]="rate", optional args[1]=rowsPerSecond (int)
        boolean useRateSource = args.length > 0 && "rate".equalsIgnoreCase(args[0]);
        String host = useRateSource ? null : (args.length > 0 ? args[0] : "localhost");
        int port = useRateSource ? -1 : (args.length > 1 ? Integer.parseInt(args[1]) : 9999);
        int rate = useRateSource && args.length > 1 ? Integer.parseInt(args[1]) : 1;

        SparkSession spark = SparkSession
                .builder()
                .appName("NetworkWordCount")
                .master(System.getProperty("spark.master", "local[*]"))
                .getOrCreate();

        Dataset<String> lines;
        if (useRateSource) {
            // Built-in generator to avoid socket listener issues
            lines = spark
                    .readStream()
                    .format("rate")
                    .option("rowsPerSecond", rate)
                    .load()
                    .selectExpr("CAST(value AS STRING)")
                    .as(Encoders.STRING());
        } else {
            lines = spark
                    .readStream()
                    .format("socket")
                    .option("host", host)
                    .option("port", port)
                    .load()
                    .as(Encoders.STRING());
        }

        Dataset<String> words = lines.flatMap(
                (String x) -> Arrays.asList(x.split(" ")).iterator(),
                Encoders.STRING());

        Dataset<org.apache.spark.sql.Row> wordCounts = words.groupBy("value").count();

        StreamingQuery query = wordCounts.writeStream()
                .outputMode("complete")
                .format("console")
                .trigger(Trigger.ProcessingTime("1 second"))
                .start();

        query.awaitTermination();
    }
}
