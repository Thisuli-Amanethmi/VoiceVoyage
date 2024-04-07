package com.example.voicevoyageapplication;

public class UserManager {
    private static UserManager instance = null;
    private String email;
    private String username;
    private UserManager() {}

    public static UserManager getInstance() {
        if (instance == null) {
            instance = new UserManager();
        }

        return instance;
    }

    public void signIn(String username, databaseUserDetails db) {
        this.username = username;
        this.email = db.getEmail(username);
    }

    public String getUsername() {
        return username;
    }

    public String getEmail() {
        return email;
    }

    public void setUser(String email, String username) {
        this.email = email;
        this.username = username;
    }
}
