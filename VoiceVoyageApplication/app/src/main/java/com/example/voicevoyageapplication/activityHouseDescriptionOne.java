package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class activityHouseDescriptionOne extends AppCompatActivity {

    TextView greetingTextView;
    EditText leftEditText, rightEditText;
    Button nextButton, instructionsButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_description_one);

        // Initialize views
        greetingTextView = findViewById(R.id.greetingTextView);
        leftEditText = findViewById(R.id.leftEditText);
        instructionsButton = findViewById(R.id.instructions_button);
        nextButton = findViewById(R.id.next_button);

        // Retrieve the username from the intent extras
        String userName = getIntent().getStringExtra("USER_NAME");

        // Display user name in greetingTextView
        greetingTextView.setText("Hi, " + userName + " !");

        // Handle submit button click
        nextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Save answers given by the user
                String leftAnswer = leftEditText.getText().toString();
                String rightAnswer = rightEditText.getText().toString();

                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionOne.this, activityHouseDescriptionTwo.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        instructionsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Save answers given by the user
                String leftAnswer = leftEditText.getText().toString();
                String rightAnswer = rightEditText.getText().toString();

                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionOne.this, activityInstructions.class);

                // Start the next activity
                startActivity(intent);
            }
        });
    }
}

