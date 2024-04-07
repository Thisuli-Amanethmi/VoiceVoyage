package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class activityChangeLoginInfo extends AppCompatActivity {

    // Button button_register, button_layout, button_instruction, button_navigation, button_settings;
    Button btnBack, btnChangeInfo;
    EditText txtUsername, txtEmail, txtPassword, txtNewPassword, txtConfirmPassword;
    databaseUserDetails db;
    UserManager userManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_change_login_info_screen);

        db = new databaseUserDetails(this);
        userManager = UserManager.getInstance();

        // Initialize buttons
        btnBack = findViewById(R.id.btn_back);
        btnChangeInfo = findViewById(R.id.btn_changeInfo);

        txtUsername = findViewById(R.id.txtUserName);
        txtEmail = findViewById(R.id.txtEmail);
        txtPassword = findViewById(R.id.txtPassword);
        txtNewPassword = findViewById(R.id.txtNewPassword);
        txtConfirmPassword = findViewById(R.id.txtConfirmPassword);

        txtUsername.setText(userManager.getUsername());
        txtEmail.setText(userManager.getEmail());
        txtEmail.setEnabled(false);

        btnBack.setOnClickListener(v -> {
            Intent intent = new Intent(activityChangeLoginInfo.this, activitySettings.class);
            startActivity(intent);
        });

        // Handle submit button click
        btnChangeInfo.setOnClickListener(v -> {
            String username = txtUsername.getText().toString();
            String email = txtEmail.getText().toString();
            String password = txtPassword.getText().toString();
            String newPassword = txtNewPassword.getText().toString();
            String confirmPassword = txtConfirmPassword.getText().toString();

            if (username.isEmpty()) {
                Toast.makeText(this, "Please enter username", Toast.LENGTH_SHORT).show();
            }

            if (!newPassword.isEmpty() && !db.checkUserNamePassword(userManager.getUsername(), password)) {
                Toast.makeText(this, "Invalid password", Toast.LENGTH_SHORT).show();
                return;
            }

            if (!newPassword.equals(confirmPassword)) {
                Toast.makeText(this, "Password does not match confirmed password", Toast.LENGTH_SHORT).show();
                return;
            }

            if (newPassword.isEmpty()) db.updateByEmail(email, username);
            else db.updateByEmail(email, username, newPassword);

            userManager.setUser(email, username);

            Toast.makeText(this, "User details updated!", Toast.LENGTH_SHORT).show();

            Intent intent = new Intent(activityChangeLoginInfo.this, activityUserHome.class);
            startActivity(intent);
        });

    }

}
