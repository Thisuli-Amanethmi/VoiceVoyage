package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class activityLogIn extends AppCompatActivity {
    private Button logInButton, backButton;
    private TextView userName, password;
    database db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        // Initialize buttons and text views
        logInButton = findViewById(R.id.button_login);
        backButton = findViewById(R.id.button_back);
        userName = findViewById(R.id.userName);
        password = findViewById(R.id.password);

        db = new database(this);

        // Handle button click
        logInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = userName.getText().toString();
                String userPassword = password.getText().toString();

                if(userName.equals("") || password.equals("")) // username & password is empty
                    Toast.makeText(activityLogIn.this, "Please enter all the fields", Toast.LENGTH_SHORT).show();
                else{
                    Boolean checkUserNamePassword = db.checkUserNamePassword(user, userPassword);

                    if(checkUserNamePassword==true) {
                        Toast.makeText(activityLogIn.this, "Log in successfull", Toast.LENGTH_SHORT).show();

                        // Pass the data to the next activity
                        Intent intent = new Intent(activityLogIn.this, activityUserHome.class);

                        // Start the next activity
                        startActivity(intent);
                    } else {
                        Toast.makeText(activityLogIn.this, "Invalid Credentials", Toast.LENGTH_SHORT).show();
                    }
                }



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
