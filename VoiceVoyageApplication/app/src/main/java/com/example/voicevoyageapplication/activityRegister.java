package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class activityRegister extends AppCompatActivity {
    private Button registerButton, backButton;
    private EditText editTextUserName, editTextEmailAddress, editTextPassword;
    databaseUserDetails db;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        // Initialize buttons and texts
        registerButton = findViewById(R.id.button_register);
        backButton = findViewById(R.id.button_back);
        editTextUserName = findViewById(R.id.editText);
        editTextEmailAddress = findViewById(R.id.editTextEmailAddress);
        editTextPassword = findViewById(R.id.editTextTextPassword);

        db = new databaseUserDetails(this);

        // Handle button click
        registerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Retrieve the data entered by the user
                String userName = editTextUserName.getText().toString();
                String emailAddress = editTextEmailAddress.getText().toString();
                String password = editTextPassword.getText().toString();

                if(userName.equals("") || emailAddress.equals("") || password.equals(""))
                    Toast.makeText(activityRegister.this, "Please enter all the fields", Toast.LENGTH_SHORT).show();
                else{
                    Boolean checkUser = db.checkUser(userName, emailAddress, password);

                    if(!checkUser){
                        Boolean checkUserName = db.checkUserName(userName); // check username

                        if(!checkUserName) { // false
                            Boolean checkUserEmail = db.checkUserName(emailAddress); // check email

                            if(!checkUserEmail) { // false
                                Boolean insert = db.insertData(userName, emailAddress, password);

                                if(insert){ // true
                                    Toast.makeText(activityRegister.this, "Registered successfully!", Toast.LENGTH_SHORT).show();

                                    // Pass the data to the next activity
                                    Intent intent = new Intent(activityRegister.this, activityHouseDescriptionOne.class);
                                    intent.putExtra("USER_NAME", userName);
                                    intent.putExtra("EMAIL_ADDRESS", emailAddress);
                                    intent.putExtra("PASSWORD", password);

                                    // Start the next activity
                                    startActivity(intent);
                                }
                                else{
                                    Toast.makeText(activityRegister.this, "Registration failed.", Toast.LENGTH_SHORT).show();
                                }
                            }
                        } else{
                            Toast.makeText(activityRegister.this, "Username already exists! Enter a new username.", Toast.LENGTH_SHORT).show();
                        }
                    } else {
                        Toast.makeText(activityRegister.this, "User already exists! please sign in.", Toast.LENGTH_SHORT).show();
                    }
                }

            }
        });

        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityRegister.this, activityFirstScreen.class);

                // Start the next activity
                startActivity(intent);

            }
        });

//        OkHttpClient client = new OkHttpClient();
//        Request request = new Request.Builder().url("http://192.168.1.12:5000/").build();
//
//        client.newCall(request).enqueue(new Callback() {
//            @Override
//            public void onFailure(Call call, IOException e) {
//                // Handle failure, and show toast on UI thread
//                runOnUiThread(new Runnable() {
//                    @Override
//                    public void run() {
//                        Toast.makeText(MainActivityRegister.this, "Network request failed :(", Toast.LENGTH_SHORT).show();
//                    }
//                });
//           }
//
//            @Override
//            public void onResponse(Call call, Response response) throws IOException {
//                // Handle response if needed
////                TextView textView=findViewById(R.id.textview);
////                textView.setText(response.body().string());
//            }
//        });
    }
}
