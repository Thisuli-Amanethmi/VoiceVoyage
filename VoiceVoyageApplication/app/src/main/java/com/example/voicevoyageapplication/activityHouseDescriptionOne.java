package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class activityHouseDescriptionOne extends AppCompatActivity {

    TextView greetingTextView;
    EditText inFrontEditText, leftEditText, farLeftEditText;
    Button nextButton, instructionsButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_description_one);

        // Initialize views
        greetingTextView = findViewById(R.id.greetingTextView);
        inFrontEditText = findViewById(R.id.inFrontEditText);
        leftEditText = findViewById(R.id.leftEditText);
        farLeftEditText = findViewById(R.id.farLeftEditText);
        instructionsButton = findViewById(R.id.agree_button);
        nextButton = findViewById(R.id.next_button);

        // Retrieve the username from the intent extras
        String userName = getIntent().getStringExtra("USER_NAME");

        // Display user name in greetingTextView
        // greetingTextView.setText("Hi, " + userName + " !");

        // Handle button click
        nextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Retrieve the data entered by the user
                String inFrontObject = inFrontEditText.getText().toString();
                String leftObject = leftEditText.getText().toString();
                String farLeftObject = farLeftEditText.getText().toString();

                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionOne.this, activityHouseDescriptionTwo.class);
                intent.putExtra("USER_NAME", userName);
                intent.putExtra("IN_FRONT_OBJECT", inFrontObject);
                intent.putExtra("LEFT_OBJECT", leftObject);
                intent.putExtra("FAR_LEFT_OBJECT", farLeftObject);

                // Start the next activity
                startActivity(intent);
            }
        });

        instructionsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionOne.this, activityInstructions.class);

                // Start the next activity
                startActivity(intent);
            }
        });
    }
}

