package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

 import java.util.ArrayList;

public class activityHomeStructureConfirmation extends AppCompatActivity {
    Button button_change, button_confirm;
    ImageView imageViewFront, imageViewLeft, imageViewFarLeft, imageViewRight, imageViewFarRight, imageViewCenter, imageViewBehind;

    // creating the objects list
    ArrayList<String> objectsList = new ArrayList<>();

    public void setObjectsList(ArrayList<String> objectsList) {
        this.objectsList = objectsList;

        objectsList.add("bed"); objectsList.add("bookshelf"); objectsList.add("chair"); objectsList.add("clothesrack");
        objectsList.add("coffeetable"); objectsList.add("commode"); objectsList.add("cupboard"); objectsList.add("door");
        objectsList.add("dressingtable"); objectsList.add("lamp"); objectsList.add("oven"); objectsList.add("pantrycupboards");
        objectsList.add("refrigerator"); objectsList.add("shoerack"); objectsList.add("sink"); objectsList.add("sofa");
        objectsList.add("staircase"); objectsList.add("stove"); objectsList.add("table"); objectsList.add("tv");
        objectsList.add("wallart"); objectsList.add("washingmachine"); objectsList.add("window");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_layout_confirmation_screen);

        // Initialize ImageView objects
        imageViewFront = findViewById(R.id.imageViewFront);
        imageViewLeft = findViewById(R.id.imageViewLeft);
        imageViewFarLeft = findViewById(R.id.imageViewFarLeft);
        imageViewRight = findViewById(R.id.imageViewRight);
        imageViewFarRight = findViewById(R.id.imageViewFarRight);
        imageViewCenter = findViewById(R.id.imageViewCenter);
        imageViewBehind = findViewById(R.id.imageViewBehind);

        // Retrieve the username from the intent extras
        Intent intent = getIntent();
        String inFront = intent.getStringExtra("IN_FRONT_OBJECT");
        String left = intent.getStringExtra("LEFT_OBJECT");
        String farLeft = intent.getStringExtra("FAR_LEFT_OBJECT");
        String right = intent.getStringExtra("RIGHT_OBJECT");
        String farRight = intent.getStringExtra("FAR_RIGHT_OBJECT");
        String center = intent.getStringExtra("BEHIND_OBJECT");
        String behind = intent.getStringExtra("CENTER_OBJECT");

        setObjectsList(objectsList);

        // setting images
        if(objectsList.contains(inFront)){
            int inFrontImageId = getResources().getIdentifier(inFront, "drawable", getPackageName());
            imageViewFront.setImageDrawable(getResources().getDrawable(inFrontImageId));
        }

        if(objectsList.contains(left)){
            int leftImageId = getResources().getIdentifier(left, "drawable", getPackageName());
            imageViewLeft.setImageDrawable(getResources().getDrawable(leftImageId));
        }

        if(objectsList.contains(farLeft)){
            int farLeftImageId = getResources().getIdentifier(farLeft, "drawable", getPackageName());
            imageViewFarLeft.setImageDrawable(getResources().getDrawable(farLeftImageId));
        }

        if(objectsList.contains(right)){
            int rightImageId = getResources().getIdentifier(right, "drawable", getPackageName());
            imageViewRight.setImageDrawable(getResources().getDrawable(rightImageId));
        }

        if(objectsList.contains(center)){
            int centerImageId = getResources().getIdentifier(center, "drawable", getPackageName());
            imageViewCenter.setImageDrawable(getResources().getDrawable(centerImageId));
        }

        if(objectsList.contains(behind)){
            int behindImageId = getResources().getIdentifier(behind, "drawable", getPackageName());
            imageViewBehind.setImageDrawable(getResources().getDrawable(behindImageId));
        }

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
