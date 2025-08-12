from flask import Blueprint, request, redirect, url_for, session

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # load data from forms
        user = request.form['user']
        pwd = request.form['pwd']

        session['user'] = user
        session['token'] = '0000'

        # return redirect('/user/dashboard')
        return redirect(url_for('user.root'))

    return '''
        <html lang="pt-BR">
        <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Login</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
        <style>
            :root{
            --bg:#0f172a;
            --card:#0b1220;
            --muted:#94a3b8;
            --accent:#7c3aed;
            --error:#ef4444;
            }
            *{box-sizing:border-box}
            html,body{height:100%;margin:0}
            body{
            display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,#071124 0%, #071a2a 55%);
            font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial;
            color:#e6eef8;padding:20px;
            }

            .login-card{
            width:100%;max-width:400px;padding:32px;border-radius:16px;
            background:linear-gradient(180deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));
            border:1px solid rgba(255,255,255,0.03);
            box-shadow:0 10px 30px rgba(2,6,23,0.6);
            }

            h1{margin-top:0;margin-bottom:20px;font-size:22px;text-align:center}

            label{display:block;margin-bottom:6px;font-weight:500}
            input[type="text"],input[type="password"]{
            width:100%;padding:12px 14px;margin-bottom:14px;
            border-radius:10px;border:1px solid rgba(255,255,255,0.04);
            background:transparent;color:inherit;font-size:15px;outline:none;
            }
            input[type="text"]:focus,input[type="password"]:focus{
            border-color:var(--accent);
            box-shadow:0 0 0 2px rgba(124,58,237,0.3);
            }

            button{
            width:100%;padding:12px;border-radius:10px;border:none;
            background:linear-gradient(90deg,var(--accent),#4f46e5);
            color:white;font-weight:600;cursor:pointer;font-size:15px;
            box-shadow:0 8px 20px rgba(79,70,229,0.18);
            }

            .muted{text-align:center;color:var(--muted);font-size:13px;margin-top:16px}
            .muted a{color:var(--accent);text-decoration:none}
        </style>
        </head>
        <body>
        <div class="login-card">
            <h1>Entrar</h1>
            <form method="POST">
            <label for="user">Usuário</label>
            <input id="user" type="text" name="user" required />

            <label for="pwd">Senha</label>
            <input id="pwd" type="password" name="pwd" required />

            <button type="submit">Entrar</button>
            </form>
            <div class="muted">Não tem conta? <a href="#">Cadastre-se</a></div>
        </div>
        </body>
        </html>

    '''