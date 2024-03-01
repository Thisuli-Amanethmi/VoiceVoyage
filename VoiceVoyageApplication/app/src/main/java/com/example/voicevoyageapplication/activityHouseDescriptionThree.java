package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class activityHouseDescriptionThree extends AppCompatActivity {
    Button previousButton, registerButton;
    EditText windorNearDoorEditText, windowLeftEditText, windorRightEditText, windowFrontEditText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_description_three);

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
                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionThree.this, activityHomeStructureConfirmation.class);

                // Start the next activity
                startActivity(intent);
            }
        });
    }
}
