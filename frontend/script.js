// تسجيل مستخدم جديد
function registerUser(name, email, password) {
    fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}

// تسجيل الدخول
function loginUser(email, password) {
    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}
<h2>التسجيل</h2>
<form onsubmit="event.preventDefault(); registerUser(
    document.getElementById('reg_name').value,
    document.getElementById('reg_email').value,
    document.getElementById('reg_password').value)">
    
    <input type="text" id="reg_name" placeholder="الاسم" required><br>
    <input type="email" id="reg_email" placeholder="البريد الإلكتروني" required><br>
    <input type="password" id="reg_password" placeholder="كلمة المرور" required><br>
    <button type="submit">تسجيل</button>
</form>

<h2>تسجيل الدخول</h2>
<form onsubmit="event.preventDefault(); loginUser(
    document.getElementById('login_email').value,
    document.getElementById('login_password').value)">
    
    <input type="email" id="login_email" placeholder="البريد الإلكتروني" required><br>
    <input type="password" id="login_password" placeholder="كلمة المرور" required><br>
    <button type="submit">دخول</button>
</form>

<script src="script.js"></script>
