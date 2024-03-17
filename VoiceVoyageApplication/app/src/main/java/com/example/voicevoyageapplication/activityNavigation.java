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
    TextView textView_status; // Added for displaying status

    private boolean isDetectionRunning = false; // Flag to track detection state

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_object_detection_and_navigation_screen);

        // Initialize buttons and TextView
        button_back = findViewById(R.id.button_back);
        button_start_detection = findViewById(R.id.button_start_detection); // Assuming a new button added
        button_stop_detection = findViewById(R.id.button_stop_detection); // Assuming a new button added
        textView_status = findViewById(R.id.textView4); // Assuming TextView displays status

        // Handle button click for navigating back (same as before)
        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                stopDetection(); // Call stopDetection before navigating back
                Intent intent = new Intent(activityNavigation.this, activityUserHome.class);
                startActivity(intent);
            }
        });

        // Handle button click for starting detection
        button_start_detection.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!isDetectionRunning) {
                    startDetection();
                    textView_status.setText("Detection Running");
                }
            }
        });

        // Handle button click for stopping detection (optional)
        button_stop_detection.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                stopDetection();
                textView_status.setText("Detection Stopped");
            }
        });
    }

    private void startDetection() {
        isDetectionRunning = true;
        new HttpGetTask().execute("http://192.168.1.12:5000/start_detection");
    }

    private void stopDetection() {
        isDetectionRunning = false;
        new HttpGetTask().execute("http://192.168.1.12:5000/stop_detection");
    }

    // AsyncTask to handle HTTP GET requests to the Flask server (consider using a library for network calls)
    private class HttpGetTask extends AsyncTask<String, Void, String> {

        @Override
        protected String doInBackground(String... urls) {
            String urlString = urls[0];
            try {
                URL url = new URL(urlString);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");
                conn.setDoOutput(true);

                BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                StringBuilder sb = new StringBuilder();
                String line;

                while ((line = reader.readLine()) != null) {
                    sb.append(line).append("\n");
                }

                reader.close();
                return sb.toString().trim();
            } catch (Exception e) {
                Log.e("HttpGetTask", "Error: " + e.getMessage());
                return null;
            }
        }

        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            // Handle the response from the server (if needed)
            if (result != null) {
                Log.i("HttpGetTask", "Response: " + result);
            }
        }
    }
}
