package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class activityFirstScreen extends AppCompatActivity {
    private Button logInButton, registerButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_first_screen);

        logInButton = findViewById(R.id.button_login);
        registerButton = findViewById(R.id.button_register);

        logInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityFirstScreen.this, activityLogIn.class);

                // Start the next activity
                startActivity(intent);

            }
        });

        registerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityFirstScreen.this, activityRegister.class);

                // Start the next activity
                startActivity(intent);

            }
        });

//        // Inside mainActivity after the user has successfully logged in or completed setup
//        Intent intent = new Intent(activityFirstScreen.this, activityUserHome.class);
//        startActivity(intent);
//        finish(); // Finish the mainActivity to prevent returning to it

    }
}
