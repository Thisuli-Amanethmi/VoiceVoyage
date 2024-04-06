package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class activityHouseDescriptionThree extends AppCompatActivity {
    Button previousButton, registerButton;
    EditText windorNearDoorEditText, windowLeftEditText, windorRightEditText, windowFrontEditText;

    databaseOntology db;

    // variables to store intent extras
    String userName, inFront, left, farLeft, right, farRight, center, behind;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_description_three);

        // Retrieve the username from the intent extras
        Intent intent = getIntent();
        if (intent != null) {
            userName = getIntent().getStringExtra("USER_NAME");
            inFront = getIntent().getStringExtra("IN_FRONT_OBJECT");
            left = getIntent().getStringExtra("LEFT_OBJECT");
            farLeft = getIntent().getStringExtra("FAR_LEFT_OBJECT");
            right = getIntent().getStringExtra("RIGHT_OBJECT");
            farRight = getIntent().getStringExtra("FAR_RIGHT_OBJECT");
            center = getIntent().getStringExtra("BEHIND_OBJECT");
            behind = getIntent().getStringExtra("CENTER_OBJECT");
        }

        db = new databaseOntology(this);

        // Initialize views
        windorNearDoorEditText = findViewById(R.id.windorNearDoorEditText);
        windowLeftEditText = findViewById(R.id.windowLeftEditText);
        windorRightEditText = findViewById(R.id.windorRightEditText);
        windowFrontEditText = findViewById(R.id.windowFrontEditText);
        previousButton = findViewById(R.id.previous_button);
        registerButton = findViewById(R.id.register_button);

        // Handle button click
        previousButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionThree.this, activityHouseDescriptionTwo.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        registerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Retrieve the data entered by the user
                String windowNearDoor = windorNearDoorEditText.getText().toString();
                String windowLeft = windowLeftEditText.getText().toString();
                String windowRight = windorRightEditText.getText().toString();
                String windowFront = windowFrontEditText.getText().toString();

                roomFormat(inFront, left, farLeft, right, farRight, behind, center, windowNearDoor, windowLeft, windowRight, windowFront);

                Boolean insert = db.insertDataMap(userName, inFront, left, farLeft, right, farRight, behind, center);

                if(insert){ // true
                    Toast.makeText(activityHouseDescriptionThree.this, "House details entered successfully!", Toast.LENGTH_SHORT).show();

                    // Pass the data to the next activity
                    Intent intent = new Intent(activityHouseDescriptionThree.this, activityHomeStructureConfirmation.class);
                    intent.putExtra("IN_FRONT_OBJECT", inFront);
                    intent.putExtra("LEFT_OBJECT", left);
                    intent.putExtra("FAR_LEFT_OBJECT", farLeft);
                    intent.putExtra("RIGHT_OBJECT", right);
                    intent.putExtra("FAR_RIGHT_OBJECT", farRight);
                    intent.putExtra("BEHIND_OBJECT", behind);
                    intent.putExtra("CENTER_OBJECT", center);

                    // Start the next activity
                    startActivity(intent);
                }
                else{
                    Toast.makeText(activityHouseDescriptionThree.this, "Re-enter house details.", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    private void roomFormat(String inFront, String left, String farLeft, String right, String farRight, String behind, String center,
                            String windowNearDoor, String windowLeft, String windowRight, String windowFront) {
        new roomFormatSave().execute(inFront, left, farLeft, right, farRight, behind, center, windowNearDoor, windowLeft, windowRight, windowFront);
    }

    private class roomFormatSave extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... params) {
            String inFront = params[0];
            String left = params[1];
            String farLeft = params[2];
            String right = params[3];
            String farRight = params[4];
            String behind = params[5];
            String center = params[6];
            String windowNearDoor = params[7];
            String windowLeft = params[8];
            String windowRight = params[9];
            String windowFront = params[10];

            String serverUrl = "http://192.168.1.12:5000/room_format" +
                    "?in_front=" + inFront +
                    "&to_the_left=" + left +
                    "&far_left=" + farLeft +
                    "&to_the_right=" + right +
                    "&far_right=" + farRight +
                    "&behind_you=" + behind +
                    "&center=" + center +
                    "&window_near_door=" + windowNearDoor +
                    "&window_on_left_wall=" + windowLeft +
                    "&window_on_right_wall=" + windowRight +
                    "&window_on_front_wall=" + windowFront;  // home wifi

            // String serverUrl = "http://172.27.41.213:5000/room_format"; // IIT server address
            // String serverUrl = "http://127.0.0.1:5000/room_format"; // local host server address
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
                    Log.e("RoomFormatSave", "Error: HTTP " + connection.getResponseCode());
                }
                connection.disconnect();
            } catch (IOException e) {
                Log.e("RoomFormatSave", "Error: " + e.getMessage());
                e.printStackTrace();
            }

            return response;
        }
    }

}
