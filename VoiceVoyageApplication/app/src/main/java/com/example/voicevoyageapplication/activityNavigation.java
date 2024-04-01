package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class activityNavigation extends AppCompatActivity {
    Button button_back;
    Button button_start_detection, button_stop_detection;
    TextView textView_status;

    private boolean isDetectionRunning = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_object_detection_and_navigation_screen);

        // Initialize buttons and TextView
        button_back = findViewById(R.id.button_back);
        button_start_detection = findViewById(R.id.button_start_detection);
        button_stop_detection = findViewById(R.id.button_stop_detection);
        textView_status = findViewById(R.id.textView4);

        // Handle button click for navigating back
        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity (optional)
                Intent intent = new Intent(activityNavigation.this, activityUserHome.class);
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
                    textView_status.setText("Detection Running");
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
                    textView_status.setText("Detection Stopped");
                }
            }
        });
    }

    private void startDetection() {
        // Execute AsyncTask to perform object detection on a background thread
        new DetectObjectsTaskStart().execute();
    }

    private void stopDetection() {
        new DetectObjectsTaskStop().execute();
    }

    private class DetectObjectsTaskStart extends AsyncTask<Void, Void, String> {

        @Override
        protected String doInBackground(Void... voids) {
            String serverUrl = "http://192.168.1.12:5000/start_detection"; // home wifi
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

    private class DetectObjectsTaskStop extends AsyncTask<Void, Void, String> {

        @Override
        protected String doInBackground(Void... voids) {
            String serverUrl = "http://192.168.1.12:5000/stop_detection"; // home wifi
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


//    private void startDetection() {
//        new HttpGetTask().execute("http://192.168.1.12:5000/start_detection");
//        isDetectionRunning = true;
//    }

//    private void stopDetection() {
//        isDetectionRunning = false;
//        new HttpGetTask().execute("http://192.168.1.12:5000/stop_detection");
//    }

//    // AsyncTask to handle HTTP GET requests to the Flask server (consider using a library for network calls)
//    private class HttpGetTask extends AsyncTask<String, Void, String> {
//
//        @Override
//        protected String doInBackground(String... urls) {
//            String urlString = urls[0];
//            try {
//                URL url = new URL(urlString);
//                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
//                conn.setRequestMethod("GET");
//                conn.setDoOutput(true);
//
//                BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
//                StringBuilder sb = new StringBuilder();
//                String line;
//
//                while ((line = reader.readLine()) != null) {
//                    sb.append(line).append("\n");
//                }
//
//                reader.close();
//                return sb.toString().trim();
//            } catch (Exception e) {
//                Log.e("HttpGetTask", "Error: " + e.getMessage());
//                return null;
//            }
//        }
//
//        @Override
//        protected void onPostExecute(String result) {
//            super.onPostExecute(result);
//            // Handle the response from the server (if needed)
//            if (result != null) {
//                Log.i("HttpGetTask", "Response: " + result);
//            }
//        }
//    }

}
