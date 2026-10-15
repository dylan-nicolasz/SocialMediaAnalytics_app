import sqlite3
#print ("Social Media Analytics")

#Connect to the database
connection = sqlite3.connect("social_media.db")
#print ("Database created successfully")

#Create a cursor
cursor = connection.cursor()

#Create the posts table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT NOT NULL,
        content TEXT NOT NULL,
        likes INTEGER DEFAULT 0,
        comments INTEGER DEFAULT 0,
        shares INTEGER DEFAULT 0,
        post_date DATE NOT NULL
    )
""")

connection.commit() 

# Add post function
def add_post ():
    platform = input ("Platform: ")
    content = input ("Content: ")
    likes= int(input ("Likes: "))
    comments = int(input ("Comments: "))
    shares = int(input ("Shares: "))
    post_date = input ("Post Date (YYYY-MM-DD): ")

    cursor.execute ("""
        INSERT INTO posts
        (platform, content, likes, comments, shares, post_date)
        VALUES (?, ?, ?, ?, ?, ?)
""", (platform, content, likes, comments, shares, post_date))

    connection.commit()
    print ("Post created successfully!")



#Retrieve posts
def view_posts():

    print ("\n====All Posts====")
    cursor.execute ("Select * FROM posts")


    posts = cursor.fetchall()

    for post in posts :
        print (f"ID: {post[0]}")
        print (f"Platform: {post[1]}")
        print (f"Content: {post[2]}")
        print (f"Likes: {post[3]}")
        print (f"Comments: {post[4]}")
        print (f"Shares: {post[5]}")
        print (f"Post Date: {post[6]}")




#Update Posts
def update_post() :

    post_id = input ("Enter post ID: ")

    def show_update_result():
        if cursor.rowcount > 0:
            print("Post updated successfully!")
        else:
            print("Post not found.")
            update_post()

    def update_platform():
        new_platform = input("Enter the new platform: ")

        cursor.execute("""
            UPDATE posts
            SET platform = ?
            WHERE id = ?
        """, (new_platform, post_id))
        connection.commit()
        show_update_result()

    def update_content ():
        new_content = input("Enter the new content: ")

        cursor.execute("""
            UPDATE posts
            SET content = ?
            WHERE id = ?
        """, (new_content, post_id))
        connection.commit()
        show_update_result()

    def update_likes():
        new_likes = int(input("Enter the new number of Likes: "))

        cursor.execute ("""
            UPDATE posts
            SET likes = ?
            WHERE id = ?
        
        """, (new_likes, post_id))

        connection.commit()
        show_update_result()

    def update_comments():
        new_comments = int(input("Enter the new number of comments: "))

        cursor.execute("""
            UPDATE posts
            SET comments = ?
            WHERE id = ?

        """, (new_comments, post_id))
        connection.commit()
        show_update_result()

    def update_shares():
        new_shares = int(input("Enter the new number of shares: "))

        cursor.execute("""
            UPDATE posts
            SET shares = ?
            WHERE id = ?
        """, (new_shares, post_id))
        connection.commit()
        show_update_result()

    def update_postDate():
        new_date = input("Enter the new date (YYYY-MM-DD): ")

        cursor.execute("""
            UPDATE posts
            SET post_date = ?
            WHERE id = ?
        """, (new_date, post_id))
        connection.commit()
        show_update_result()



    while True:
        print ("\n--------------")
        print ("What would you like to update?")
        print("1. Platform")
        print("2. Content")
        print("3. Likes")
        print("4. Comments")
        print("5. Share")
        print("6. Post Date")
        print("7. Exit")
       

        choice = input("\nChoose an option: ")

        if choice == "1":
            update_platform()

        elif choice == "2":
            update_content()

        elif choice == "3":
            update_likes()

        elif choice == "4":
            update_comments()

        elif choice == "5":
            update_shares()

        elif choice == "6":
            update_postDate()

        elif choice == "7":
            print("Returning to main menu...")
            break

        else:
            print("Invalid option. Please try again.")

    


#Delete a post
def delete_post():
    delete_id= input ("Enter the ID of the post you want to delete: ")
    cursor.execute ("""
        DELETE FROM posts
        WHERE id = ?
    """, (delete_id))

    connection.commit()
    print ("Posts deleted successdully!")

#Analytics report

def analytics_report ():
    print ("----Analytics Report----")

    cursor.execute("""
        SELECT
            COUNT(*) AS total_posts,
            SUM(likes) AS total_likes,
            AVG(likes) AS avg_likes,
            SUM(comments) AS total_comments,
            AVG(comments) AS avg_comments,
            SUM(shares) AS total_shares
        FROM posts
""")

    report = cursor.fetchone()

    print("\nPOST SUMMARY")
    print("----------------------------------------")
    print(f"Total Posts:       {report[0]}")

    print("\nENGAGEMENT")
    print("----------------------------------------")
    print(f"Total Likes:       {report[1]}")
    print(f"Average Likes:     {report[2]:.2f}")
    print(f"Total Comments:    {report[3]}")
    print(f"Average Comments:  {report[4]:.2f}")
    print(f"Total Shares:      {report[5]}")

    print("\n========================================")

    connection.commit()



def show_menu():
    while True:
        print("\n================================")
        print("     SOCIAL MEDIA ANALYTICS")
        print("================================")
        print("1. Add Post")
        print("2. View Posts")
        print("3. Update Post")
        print("4. Delete Post")
        print("5. Analytics Report")
        print("6. Exit") 

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_post()

        elif choice == "2":
            view_posts()

        elif choice == "3":
            update_post()

        elif choice == "4":
            delete_post()

        elif choice == "5":
            analytics_report()

        elif choice == "6":
            print ("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


show_menu()

connection.close()
