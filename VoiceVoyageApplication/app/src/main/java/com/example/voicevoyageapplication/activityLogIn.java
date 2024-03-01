package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class activityLogIn extends AppCompatActivity {
    private Button logInButton, backButton;
    // private TextView

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        // Initialize buttons
        logInButton = findViewById(R.id.button_login);
        backButton = findViewById(R.id.button_back);

        // Handle button click
        // if  login info correct --> login button on click
        // else ---> notice
        logInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityLogIn.this, activityUserHome.class);

                // Start the next activity
                startActivity(intent);

            }
        });

        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityLogIn.this, activityFirstScreen.class);

                // Start the next activity
                startActivity(intent);

            }
        });
    }
}
