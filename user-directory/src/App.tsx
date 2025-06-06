import React, { useEffect, useState } from 'react';
import styles from './UserDirectory.module.css';
import { User } from './types';
import UserTable from './UserTable';
import UserModal from './UserModal';

const USERS_API = 'https://jsonplaceholder.typicode.com/users';

const App: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUser, setSelectedUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch(USERS_API)
      .then(res => res.json())
      .then(data => {
        setUsers(data);
        setLoading(false);
      })
      .catch(() => {
        setError('Failed to load users');
        setLoading(false);
      });
  }, []);

  const handleDelete = (id: number) => {
    setUsers(users => users.filter(u => u.id !== id));
    if (selectedUser && selectedUser.id === id) setSelectedUser(null);
  };

  return (
    <div className={styles.container}>
      <div className={styles.title}>Users</div>
      {loading && <div>Loading...</div>}
      {error && <div style={{color: 'red'}}>{error}</div>}
      {!loading && !error && (
        <UserTable users={users} onUserClick={setSelectedUser} onDelete={handleDelete} />
      )}
      {selectedUser && (
        <UserModal user={selectedUser} onClose={() => setSelectedUser(null)} />
      )}
    </div>
  );
};

export default App;
