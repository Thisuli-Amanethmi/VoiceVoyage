package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class activityHomeStructureConfirmation extends AppCompatActivity {
    Button button_change, button_confirm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_layout_confirmation_screen);

        // Initialize buttons
        button_confirm = findViewById(R.id.confirm_button);
        button_change = findViewById(R.id.change_button);

        // Handle button click
        button_change.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityHomeStructureConfirmation.this, activityHouseDescriptionOne.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        button_confirm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityHomeStructureConfirmation.this, activityUserHome.class);

                // Start the next activity
                startActivity(intent);
            }
        });
    }
}
