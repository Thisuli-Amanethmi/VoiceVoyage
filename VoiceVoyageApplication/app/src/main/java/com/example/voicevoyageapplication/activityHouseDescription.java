package com.example.voicevoyageapplication;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class activityHouseDescription extends AppCompatActivity {

    TextView greetingTextView;
    EditText leftEditText, rightEditText;
    Button submitButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_description);

        // Initialize views
        greetingTextView = findViewById(R.id.greetingTextView);
        leftEditText = findViewById(R.id.leftEditText);
        rightEditText = findViewById(R.id.rightEditText);
        submitButton = findViewById(R.id.button);

        // Retrieve the username from the intent extras
        String userName = getIntent().getStringExtra("USER_NAME");

        // Display user name in greetingTextView
        greetingTextView.setText("Hi, " + userName + " !");

        // Handle submit button click
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Save answers given by the user
                String leftAnswer = leftEditText.getText().toString();
                String rightAnswer = rightEditText.getText().toString();

                // You can save the answers to SharedPreferences, a database, or any other storage mechanism

                // Navigate to a new page
                // Intent intent = new Intent(HouseDescription.this, NextActivity.class);
                // startActivity(intent);
            }
        });
    }
}

