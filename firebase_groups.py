# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# # Initialize Firebase Admin with your service account key
# cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
# firebase_admin.initialize_app(cred)

# # Initialize Firestore client
# db = firestore.client()

# def fetch_specific_group(group_id):
#     group_ref = db.collection('groups').document(group_id)
#     group = group_ref.get()
    
#     if group.exists:
#         group_data = group.to_dict()
        
#         print(f"\nGroup ID: {group.id}")
#         print(f"Interests: {group_data.get('Interests', [])}")
#         print(f"Dynamic: {group_data.get('Dynamic', {})}")
#         print(f"Previous Questions: {group_data.get('previousQuestions', [])}")
#     else:
#         print(f"No group found with ID: {group_id}")

# if __name__ == "__main__":
#     fetch_specific_group('your_group_id') 