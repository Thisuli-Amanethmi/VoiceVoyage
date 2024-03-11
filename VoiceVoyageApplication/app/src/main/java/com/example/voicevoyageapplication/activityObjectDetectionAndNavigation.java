package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONObject;

import java.net.HttpURLConnection;
import java.net.URL;

public class activityObjectDetectionAndNavigation extends AppCompatActivity {
    Button button_back;
    Button button_start_detection;
    Button button_stop_detection;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_object_detection_and_navigation_screen);

        // Initialize buttons
        button_back = findViewById(R.id.button_back);
        button_start_detection = findViewById(R.id.button_stop_detection);
        button_stop_detection = findViewById(R.id.button_stop_detection);

        // Handle button click for navigating back
        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityObjectDetectionAndNavigation.this, activityUserHome.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        // Handle button click for starting object detection
        button_start_detection.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Start object detection
                new ObjectDetectionTask().execute("start");
            }
        });

        // Handle button click for stopping object detection
        button_stop_detection.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Stop object detection
                new ObjectDetectionTask().execute("stop");
            }
        });
    }

    // AsyncTask to trigger object detection via Flask server
    private static class ObjectDetectionTask extends AsyncTask<String, Void, Void> {
        @Override
        protected Void doInBackground(String... params) {
            try {
                // Create a JSON object with necessary data
                JSONObject postData = new JSONObject();
                // You can add more parameters if needed

                // Specify the Flask server URL
                URL url = new URL("http://192.168.1.12:5000/" + params[0] + "_detection");

                // Open connection
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("GET");
                connection.setRequestProperty("Content-Type", "application/json");
                connection.setDoOutput(true);

                // Send GET request
                connection.connect();

                // Get response
                int responseCode = connection.getResponseCode();
                Log.d("Response Code", String.valueOf(responseCode));

                // Close connection
                connection.disconnect();
            } catch (Exception e) {
                e.printStackTrace();
            }
            return null;
        }
    }

}
