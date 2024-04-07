package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class activitySettings extends AppCompatActivity {
    // Button button_register, button_layout, button_instruction, button_navigation, button_settings;
    Button btnChangeLayout, btnChangeLoginInfo, btnBack;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings_screen);

        // Initialize buttons
        btnChangeLoginInfo = findViewById(R.id.btn_changeInfo);
        btnChangeLayout = findViewById(R.id.btn_changeLayout);
        btnBack = findViewById(R.id.btn_back);

        btnBack.setOnClickListener(v -> {
            Intent intent = new Intent(activitySettings.this, activityUserHome.class);
            startActivity(intent);
        });

        btnChangeLayout.setOnClickListener(v -> {
            Intent intent = new Intent(activitySettings.this, activityHouseDescriptionOne.class);
            UserManager userManager = UserManager.getInstance();
            intent.putExtra("USER_NAME", userManager.getUsername());
            intent.putExtra("EMAIL_ADDRESS", userManager.getEmail());
            startActivity(intent);
        });

        btnChangeLoginInfo.setOnClickListener(v -> {
            Intent intent = new Intent(activitySettings.this, activityChangeLoginInfo.class);
            startActivity(intent);
        });
    }
}
