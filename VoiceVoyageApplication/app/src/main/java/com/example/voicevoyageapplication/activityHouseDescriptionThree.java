package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

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
}
