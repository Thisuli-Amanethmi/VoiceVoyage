package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class activityObjectDetectionAndNavigation extends AppCompatActivity {

    Button button_back;
    Button button_start_detection;
    Button button_stop_detection;
    TextView textView_detectionResults;
    boolean isDetectionRunning = false; // Flag to track detection state

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_object_detection_and_navigation_screen);

        // Initialize buttons and text view
        button_back = findViewById(R.id.button_back);
        button_start_detection = findViewById(R.id.button_start_detection);
        button_stop_detection = findViewById(R.id.button_stop_detection);
        textView_detectionResults = findViewById(R.id.textView4);

        // Handle button click for navigating back
        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity (optional)
                Intent intent = new Intent(activityObjectDetectionAndNavigation.this, activityUserHome.class);
                startActivity(intent);

                // Stop detection if running
                if (isDetectionRunning) {
                    stopDetection();
                }
            }
        });

        // Handle button click for starting detection
        button_start_detection.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!isDetectionRunning) {
                    startDetection();
                    isDetectionRunning = true;
                }
            }
        });

        // Handle button click for stopping detection
        button_stop_detection.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isDetectionRunning) {
                    stopDetection();
                    isDetectionRunning = false;
                }
            }
        });
    }

    private void startDetection() {
        // Execute AsyncTask to perform object detection on a background thread
        new DetectObjectsTask().execute();
    }

    private void stopDetection() {
        // Implement logic to stop detection if needed (might not be necessary with Flask)
        // You can remove objects from the view or display a message here
        textView_detectionResults.setText("Detection Stopped");
    }

    private class DetectObjectsTask extends AsyncTask<Void, Void, String> {

        @Override
        protected String doInBackground(Void... voids) {
            String serverUrl = "http://192.168.1.12:5000/detect_objects"; // IIT server address
            // String serverUrl = "http://172.27.41.213:5000/detect_objects"; // IIT server address
            // String serverUrl = "http://127.0.0.1:5000/detect_objects"; // local host server address
            String response = "";

            try {
                URL url = new URL(serverUrl);
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("GET");
                connection.setRequestProperty("Content-Type", "application/json; charset=utf-8");

                // Handle connection and response
                if (connection.getResponseCode() == HttpURLConnection.HTTP_OK) {
                    BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                    StringBuilder stringBuilder = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        stringBuilder.append(line).append("\n");
                    }
                    reader.close();
                    response = stringBuilder.toString();

                    Log.d("NET", response);
                } else {
                    Log.e("ObjectDetection", "Error: HTTP " + connection.getResponseCode());
                }
                connection.disconnect();
            } catch (IOException e) {
                Log.e("ObjectDetection", "Error: " + e.getMessage());
                e.printStackTrace();
            }

            return response;
        }
    }
}
