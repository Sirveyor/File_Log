
## **1. Start of Every Session**
### **Pull the latest changes**
**GUI:**  
Source Control → `…` → **Pull**

**Command Palette:**  
`Git: Pull`

**Terminal:**
```
git pull
```

---

## **2. Working on Code**
### **View changes**
- Open the **Source Control** panel  
- Click any file to view diffs

### **Stage changes**
**GUI:**  
- Click **+** next to a file  
- Or click **+** next to “Changes” to stage all  

**Terminal:**
```
git add .
```

### **Commit changes**
**GUI:**  
- Type a message in the commit box  
- Press **Ctrl+Enter**

**Terminal:**
```
git commit -m "Your message"
```

---

## **3. Push Your Work**
**GUI:**  
Click **Sync Changes** (bottom-left)

**Command Palette:**  
`Git: Push`

**Terminal:**
```
git push
```

---

## **4. Branching**
### **Create a new branch**
**GUI:**  
Click branch name (bottom-left) → **Create new branch**

**Terminal:**
```
git checkout -b feature-name
```

### **Switch branches**
**GUI:**  
Click branch name → choose branch

**Terminal:**
```
git checkout main
```

### **Merge a branch**
**Command Palette:**  
`Git: Merge Branch`

**Terminal:**
```
git checkout main
git pull
git merge feature-name
git push
```

---

## **5. WIP (Work In Progress)**
### **Quick WIP commit**
```
git add .
git commit -m "WIP: partial refactor"
git push
```

### **WIP branch**
```
git checkout -b wip-watcher-refactor
git add .
git commit -m "WIP: watcher refactor"
git push
```

---

## **6. Clean Workspace Habits**
### **Check status**
```
git status
```

### **Stash changes (if needed)**
**GUI:**  
Source Control → `…` → **Stash**

**Terminal:**
```
git stash
git pull
git stash pop
```

---

## **7. Daily Rhythm (Home ↔ Work)**
1. **Pull**  
2. **Code**  
3. **Commit**  
4. **Push**

This keeps both machines perfectly in sync.

---

If you want, I can also produce a **minimalist black‑and‑white version**, a **two‑column version**, or a **laminated desk card layout**.
