import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os
from datetime import datetime
from PIL import Image, ImageTk  # 需要安装: pip install pillow

class RestaurantSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("餐厅管理系统")
        self.root.geometry("900x650")
        
        # 设置应用程序图标和主题
        self.set_theme()
        
        # 初始化数据文件
        self.initialize_data_files()
        
        # 显示登录界面
        self.show_login_frame()
    
    def set_theme(self):
        # 创建自定义样式
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#F5F5F5")
        self.style.configure("TLabel", background="#F5F5F5", font=("微软雅黑", 10))
        self.style.configure("TButton", font=("微软雅黑", 10))
        self.style.configure("Header.TLabel", font=("微软雅黑", 16, "bold"), background="#F0F0F0")
        self.style.configure("Title.TLabel", font=("微软雅黑", 20, "bold"), background="#F5F5F5")
        
        # 表格样式
        self.style.configure("Treeview", 
                             background="#FFFFFF",
                             fieldbackground="#FFFFFF",
                             foreground="black",
                             font=("微软雅黑", 9))
        self.style.configure("Treeview.Heading", 
                             font=("微软雅黑", 10, "bold"),
                             background="#4A7DAC",
                             foreground="white")
        self.style.map('Treeview', background=[('selected', '#4A7DAC')])
        
        # 设置窗口背景色
        self.root.configure(background="#F5F5F5")
        
        # 加载通用图标和资源
        try:
            img = Image.open("icons/restaurant_icon.png")
            img = img.resize((32, 32), Image.LANCZOS)
            self.app_icon = ImageTk.PhotoImage(img)
            self.root.iconphoto(False, self.app_icon)
        except:
            print("警告: 未能加载应用图标")
            
    def initialize_data_files(self):
        # 检查并创建数据文件
        if not os.path.exists("users.json"):
            with open("users.json", "w", encoding="utf-8") as f:
                json.dump({"users": [], "admins": []}, f, ensure_ascii=False)
        
        if not os.path.exists("menu.json"):
            with open("menu.json", "w", encoding="utf-8") as f:
                json.dump({"items": []}, f, ensure_ascii=False)
        
        if not os.path.exists("orders.json"):
            with open("orders.json", "w", encoding="utf-8") as f:
                json.dump({"orders": []}, f, ensure_ascii=False)
    
    def clear_window(self):
        # 清除当前窗口中的所有控件
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login_frame(self):
        self.clear_window()
        
        # 创建主框架
        main_frame = ttk.Frame(self.root, style="TFrame")
        main_frame.pack(fill="both", expand=True)
        
        # 创建登录框架
        login_frame = ttk.Frame(main_frame, padding=30, style="TFrame")
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # 装饰线条
        header_line = ttk.Separator(login_frame, orient="horizontal")
        header_line.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5, 20))
        
        # 标题
        ttk.Label(login_frame, text="餐厅管理系统", style="Title.TLabel").grid(row=0, column=0, columnspan=2, pady=10)
        
        # 用户登录区域
        ttk.Label(login_frame, text="用户名:", style="TLabel").grid(row=2, column=0, sticky="e", pady=8, padx=5)
        self.username_entry = ttk.Entry(login_frame, width=25, font=("微软雅黑", 10))
        self.username_entry.grid(row=2, column=1, pady=8, padx=5)
        
        ttk.Label(login_frame, text="密码:", style="TLabel").grid(row=3, column=0, sticky="e", pady=8, padx=5)
        self.password_entry = ttk.Entry(login_frame, width=25, font=("微软雅黑", 10), show="*")
        self.password_entry.grid(row=3, column=1, pady=8, padx=5)
        
        # 按钮区域
        btn_frame = ttk.Frame(login_frame, style="TFrame")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        user_login_btn = ttk.Button(btn_frame, text="用户登录", command=self.user_login)
        user_login_btn.pack(side="left", padx=10)
        
        admin_login_btn = ttk.Button(btn_frame, text="管理员登录", command=self.admin_login)
        admin_login_btn.pack(side="left", padx=10)
        
        # 注册区域
        reg_frame = ttk.Frame(login_frame, style="TFrame")
        reg_frame.grid(row=5, column=0, columnspan=2, pady=(10, 0))
        
        register_btn = ttk.Button(reg_frame, text="用户注册", command=self.show_user_register)
        register_btn.pack(side="left", padx=10)
        
        admin_register_btn = ttk.Button(reg_frame, text="管理员注册", command=self.show_admin_register)
        admin_register_btn.pack(side="left", padx=10)
        
        # 底部装饰线条
        footer_line = ttk.Separator(login_frame, orient="horizontal")
        footer_line.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(20, 10))
        
        # 添加页脚
        ttk.Label(login_frame, text="© 2025 餐厅管理系统", style="TLabel").grid(row=7, column=0, columnspan=2, pady=5)
        
        # 设置焦点
        self.username_entry.focus()
    
    def show_user_register(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)
        
        tk.Label(frame, text="用户注册", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame, text="用户名:").grid(row=1, column=0, sticky="e", pady=5)
        self.reg_username = tk.Entry(frame, width=25)
        self.reg_username.grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="密码:").grid(row=2, column=0, sticky="e", pady=5)
        self.reg_password = tk.Entry(frame, width=25, show="*")
        self.reg_password.grid(row=2, column=1, pady=5)
        
        tk.Label(frame, text="手机号码:").grid(row=3, column=0, sticky="e", pady=5)
        self.reg_phone = tk.Entry(frame, width=25)
        self.reg_phone.grid(row=3, column=1, pady=5)
        
        tk.Button(frame, text="注册", command=self.register_user).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="返回", command=self.show_login_frame).grid(row=4, column=1, pady=10)
    
    def show_admin_register(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)
        
        tk.Label(frame, text="管理员注册", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame, text="用户名:").grid(row=1, column=0, sticky="e", pady=5)
        self.admin_reg_username = tk.Entry(frame, width=25)
        self.admin_reg_username.grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="密码:").grid(row=2, column=0, sticky="e", pady=5)
        self.admin_reg_password = tk.Entry(frame, width=25, show="*")
        self.admin_reg_password.grid(row=2, column=1, pady=5)
        
        tk.Label(frame, text="管理码:").grid(row=3, column=0, sticky="e", pady=5)
        self.admin_code = tk.Entry(frame, width=25, show="*")
        self.admin_code.grid(row=3, column=1, pady=5)
        
        tk.Button(frame, text="注册", command=self.register_admin).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="返回", command=self.show_login_frame).grid(row=4, column=1, pady=10)
    
    def register_user(self):
        username = self.reg_username.get()
        password = self.reg_password.get()
        phone = self.reg_phone.get()
        
        if not (username and password and phone):
            messagebox.showerror("错误", "所有字段都必须填写")
            return
        
        with open("users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # 检查用户名是否已存在
        for user in data["users"]:
            if user["username"] == username:
                messagebox.showerror("错误", "用户名已存在")
                return
        
        # 添加新用户
        data["users"].append({
            "username": username,
            "password": password,
            "phone": phone
        })
        
        with open("users.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        messagebox.showinfo("成功", "用户注册成功")
        self.show_login_frame()
    
    def register_admin(self):
        username = self.admin_reg_username.get()
        password = self.admin_reg_password.get()
        admin_code = self.admin_code.get()
        
        if not (username and password):
            messagebox.showerror("错误", "所有字段都必须填写")
            return
        
        # 简单的管理员验证码 (实际应用中应使用更安全的方法)
        if admin_code != "admin123":
            messagebox.showerror("错误", "管理员验证码错误")
            return
        
        with open("users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # 检查管理员名是否已存在
        for admin in data["admins"]:
            if admin["username"] == username:
                messagebox.showerror("错误", "管理员名已存在")
                return
        
        # 添加新管理员
        data["admins"].append({
            "username": username,
            "password": password
        })
        
        with open("users.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        messagebox.showinfo("成功", "管理员注册成功")
        self.show_login_frame()
    
    def user_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not (username and password):
            messagebox.showerror("错误", "请输入用户名和密码")
            return
        
        with open("users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                self.current_user = username
                self.show_user_main_menu()
                return
        
        messagebox.showerror("错误", "用户名或密码错误")
    
    def admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not (username and password):
            messagebox.showerror("错误", "请输入用户名和密码")
            return
        
        with open("users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for admin in data["admins"]:
            if admin["username"] == username and admin["password"] == password:
                self.current_admin = username
                self.show_admin_panel()
                return
        
        messagebox.showerror("错误", "管理员名或密码错误")
    
    def show_user_main_menu(self):
        self.clear_window()
        
        # 主菜单框架
        main_frame = ttk.Frame(self.root, style="TFrame")
        main_frame.pack(fill="both", expand=True)
        
        # 顶部标题栏
        title_frame = ttk.Frame(main_frame, padding=10, style="TFrame")
        title_frame.pack(fill="x")
        
        # 顶部装饰线
        header_line = ttk.Separator(title_frame, orient="horizontal")
        header_line.pack(fill="x", pady=5)
        
        header_frame = ttk.Frame(title_frame, style="TFrame")
        header_frame.pack(fill="x", pady=10)
        
        ttk.Label(header_frame, text=f"欢迎您, {self.current_user}", style="Header.TLabel").pack(side="left", padx=20)
        ttk.Button(header_frame, text="退出登录", command=self.show_login_frame).pack(side="right", padx=20)
        
        # 主内容区
        content_frame = ttk.Frame(main_frame, padding=30, style="TFrame")
        content_frame.pack(fill="both", expand=True)
        
        # 选项卡容器
        menu_frame = ttk.Frame(content_frame, style="TFrame")
        menu_frame.pack(pady=50)
        
        # 选项按钮 - 使用更现代的样式
        order_btn = tk.Button(menu_frame, text="点餐", width=20, height=2, 
                            font=("微软雅黑", 14, "bold"), bg="#4A7DAC", fg="white",
                            relief="flat", command=self.show_ordering_menu)
        order_btn.pack(pady=15)
        
        my_orders_btn = tk.Button(menu_frame, text="我的订单", width=20, height=2, 
                                font=("微软雅黑", 14, "bold"), bg="#4A7DAC", fg="white",
                                relief="flat", command=self.show_my_orders)
        my_orders_btn.pack(pady=15)
        
        # 底部装饰
        footer_frame = ttk.Frame(main_frame, padding=10, style="TFrame")
        footer_frame.pack(fill="x", side="bottom")
        
        footer_line = ttk.Separator(footer_frame, orient="horizontal")
        footer_line.pack(fill="x", pady=5)
        
        ttk.Label(footer_frame, text="© 2025 餐厅管理系统", style="TLabel").pack(side="right", padx=20, pady=5)
    
    def show_ordering_menu(self):
        self.clear_window()
        
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)
        
        # 顶部标题栏
        title_frame = tk.Frame(main_frame, bg="#f0f0f0", height=50)
        title_frame.pack(fill="x")
        
        tk.Label(title_frame, text="点餐菜单", font=("Arial", 14), bg="#f0f0f0").pack(side="left", padx=20, pady=10)
        tk.Button(title_frame, text="返回", command=self.show_user_main_menu).pack(side="right", padx=20, pady=10)
        
        # 主内容区
        content_frame = tk.Frame(main_frame)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # 创建菜单表格
        columns = ("id", "name", "price", "description", "quantity")
        self.menu_tree = ttk.Treeview(content_frame, columns=columns, show="headings")
        
        self.menu_tree.heading("id", text="ID")
        self.menu_tree.heading("name", text="菜品名称")
        self.menu_tree.heading("price", text="价格")
        self.menu_tree.heading("description", text="描述")
        self.menu_tree.heading("quantity", text="数量")
        
        self.menu_tree.column("id", width=50)
        self.menu_tree.column("name", width=150)
        self.menu_tree.column("price", width=80)
        self.menu_tree.column("description", width=300)
        self.menu_tree.column("quantity", width=80)
        
        self.menu_tree.pack(fill="both", expand=True)
        
        # 加载菜单数据
        self.load_menu_data()
        
        # 添加购物车按钮和总价显示
        control_frame = tk.Frame(main_frame)
        control_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Button(control_frame, text="添加到购物车", command=self.add_to_cart).pack(side="left", padx=5)
        tk.Button(control_frame, text="减少数量", command=self.decrease_quantity).pack(side="left", padx=5)
        tk.Button(control_frame, text="查看购物车", command=self.view_cart).pack(side="left", padx=5)
        
        self.cart_items = {}  # 初始化购物车
    
    def load_menu_data(self):
        try:
            with open("menu.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 清除现有数据(根据当前显示的页面决定使用哪个树控件)
            if hasattr(self, 'menu_tree') and self.menu_tree.winfo_exists():
                for item in self.menu_tree.get_children():
                    self.menu_tree.delete(item)
            
            # 添加新数据到用户界面
            for idx, item in enumerate(data["items"]):
                self.menu_tree.insert("", "end", values=(
                    idx+1, 
                    item["name"], 
                    f"¥{item['price']}", 
                    item["description"],
                    0
                ))
        except Exception as e:
            messagebox.showerror("错误", f"加载菜单失败: {str(e)}")
    
    def add_to_cart(self):
        selected_item = self.menu_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择菜品")
            return
        
        item_data = self.menu_tree.item(selected_item, "values")
        item_id = item_data[0]
        item_name = item_data[1]
        item_price = float(item_data[2].replace("¥", ""))
        
        # 更新表格中的数量
        current_qty = int(item_data[4])
        self.menu_tree.item(selected_item, values=(item_id, item_name, f"¥{item_price}", item_data[3], current_qty + 1))
        
        # 更新购物车数据
        if item_id in self.cart_items:
            self.cart_items[item_id]["quantity"] += 1
        else:
            self.cart_items[item_id] = {
                "name": item_name,
                "price": item_price,
                "quantity": 1
            }
    
    def decrease_quantity(self):
        selected_item = self.menu_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择菜品")
            return
        
        item_data = self.menu_tree.item(selected_item, "values")
        item_id = item_data[0]
        current_qty = int(item_data[4])
        
        if current_qty > 0:
            self.menu_tree.item(selected_item, values=(item_data[0], item_data[1], item_data[2], item_data[3], current_qty - 1))
            
            # 更新购物车数据
            if item_id in self.cart_items:
                self.cart_items[item_id]["quantity"] -= 1
                if self.cart_items[item_id]["quantity"] <= 0:
                    del self.cart_items[item_id]
    
    def view_cart(self):
        if not self.cart_items:
            messagebox.showinfo("购物车", "购物车为空")
            return
        
        cart_window = tk.Toplevel(self.root)
        cart_window.title("购物车")
        cart_window.geometry("500x400")
        
        # 创建购物车表格
        columns = ("name", "price", "quantity", "subtotal")
        cart_tree = ttk.Treeview(cart_window, columns=columns, show="headings")
        
        cart_tree.heading("name", text="菜品名称")
        cart_tree.heading("price", text="单价")
        cart_tree.heading("quantity", text="数量")
        cart_tree.heading("subtotal", text="小计")
        
        cart_tree.column("name", width=150)
        cart_tree.column("price", width=80)
        cart_tree.column("quantity", width=80)
        cart_tree.column("subtotal", width=100)
        
        cart_tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # 添加购物车项目
        total = 0
        for item_id, item_data in self.cart_items.items():
            if item_data["quantity"] > 0:
                subtotal = item_data["price"] * item_data["quantity"]
                cart_tree.insert("", "end", values=(
                    item_data["name"], 
                    f"¥{item_data['price']}", 
                    item_data["quantity"], 
                    f"¥{subtotal:.2f}"
                ))
                total += subtotal
        
        # 显示总价
        total_frame = tk.Frame(cart_window)
        total_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(total_frame, text=f"总计: ¥{total:.2f}", font=("Arial", 12, "bold")).pack(side="right")
        
        # 添加提交订单按钮
        button_frame = tk.Frame(cart_window)
        button_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Button(button_frame, text="提交订单", command=lambda: self.place_order(cart_window)).pack(side="right")
    
    def place_order(self, cart_window):
        if not self.cart_items:
            messagebox.showinfo("提示", "购物车为空，无法提交订单")
            return
        
        # 计算总金额
        total = 0
        order_items = []
        
        for item_id, item_data in self.cart_items.items():
            if item_data["quantity"] > 0:
                subtotal = item_data["price"] * item_data["quantity"]
                total += subtotal
                order_items.append({
                    "name": item_data["name"],
                    "price": item_data["price"],
                    "quantity": item_data["quantity"],
                    "subtotal": subtotal
                })
        
        # 创建订单
        try:
            with open("orders.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 添加新订单
            order_id = len(data["orders"]) + 1
            order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            new_order = {
                "order_id": order_id,
                "username": self.current_user,
                "items": order_items,
                "total": total,
                "status": "待处理",
                "order_time": order_time
            }
            
            data["orders"].append(new_order)
            
            with open("orders.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            messagebox.showinfo("成功", f"订单已提交，订单号: {order_id}")
            cart_window.destroy()
            
            # 清空购物车
            self.cart_items = {}
            self.load_menu_data()  # 重置菜单显示
            
        except Exception as e:
            messagebox.showerror("错误", f"提交订单失败: {str(e)}")
    
    def show_my_orders(self):
        self.clear_window()
        
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)
        
        # 顶部标题栏
        title_frame = tk.Frame(main_frame, bg="#f0f0f0", height=50)
        title_frame.pack(fill="x")
        
        tk.Label(title_frame, text="我的订单", font=("Arial", 14), bg="#f0f0f0").pack(side="left", padx=20, pady=10)
        tk.Button(title_frame, text="返回", command=self.show_user_main_menu).pack(side="right", padx=20, pady=10)
        
        # 主内容区
        content_frame = tk.Frame(main_frame)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # 创建订单表格
        columns = ("order_id", "time", "items", "total", "status")
        self.orders_tree = ttk.Treeview(content_frame, columns=columns, show="headings")
        
        self.orders_tree.heading("order_id", text="订单号")
        self.orders_tree.heading("time", text="下单时间")
        self.orders_tree.heading("items", text="菜品")
        self.orders_tree.heading("total", text="总计")
        self.orders_tree.heading("status", text="状态")
        
        self.orders_tree.column("order_id", width=70)
        self.orders_tree.column("time", width=150)
        self.orders_tree.column("items", width=300)
        self.orders_tree.column("total", width=80)
        self.orders_tree.column("status", width=80)
        
        self.orders_tree.pack(fill="both", expand=True)
        
        # 加载订单数据
        self.load_user_orders()
        
        # 按钮区域
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="查看订单详情", command=self.view_order_details).pack(side="left", padx=5)
        tk.Button(button_frame, text="取消订单", command=self.cancel_order).pack(side="left", padx=5)
    
    def load_user_orders(self):
        try:
            with open("orders.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 清除现有数据
            for item in self.orders_tree.get_children():
                self.orders_tree.delete(item)
            
            # 添加用户的订单
            for order in data["orders"]:
                if order["username"] == self.current_user:
                    # 生成菜品简要信息
                    items_summary = ", ".join([f"{item['name']} x{item['quantity']}" for item in order["items"]])
                    if len(items_summary) > 40:
                        items_summary = items_summary[:37] + "..."
                    
                    self.orders_tree.insert("", "end", values=(
                        order["order_id"],
                        order["order_time"],
                        items_summary,
                        f"¥{order['total']:.2f}",
                        order["status"]
                    ))
        except Exception as e:
            messagebox.showerror("错误", f"加载订单失败: {str(e)}")
    
    def view_order_details(self):
        selected_item = self.orders_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择一个订单")
            return
        
        order_id = self.orders_tree.item(selected_item, "values")[0]
        
        try:
            # 查找订单详情
            with open("orders.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            order_data = None
            for order in data["orders"]:
                if str(order["order_id"]) == order_id:
                    order_data = order
                    break
            
            if order_data:
                # 创建订单详情窗口
                details_window = tk.Toplevel(self.root)
                details_window.title(f"订单 #{order_id} 详情")
                details_window.geometry("500x400")
                
                # 订单信息
                info_frame = tk.Frame(details_window, padx=10, pady=10)
                info_frame.pack(fill="x")
                
                tk.Label(info_frame, text=f"订单号: {order_id}", font=("Arial", 12)).pack(anchor="w")
                tk.Label(info_frame, text=f"下单时间: {order_data['order_time']}", font=("Arial", 12)).pack(anchor="w")
                tk.Label(info_frame, text=f"状态: {order_data['status']}", font=("Arial", 12)).pack(anchor="w")
                
                # 菜品详情表格
                items_frame = tk.Frame(details_window, padx=10)
                items_frame.pack(fill="both", expand=True)
                
                columns = ("name", "price", "quantity", "subtotal")
                items_tree = ttk.Treeview(items_frame, columns=columns, show="headings")
                
                items_tree.heading("name", text="菜品名称")
                items_tree.heading("price", text="单价")
                items_tree.heading("quantity", text="数量")
                items_tree.heading("subtotal", text="小计")
                
                items_tree.column("name", width=150)
                items_tree.column("price", width=80)
                items_tree.column("quantity", width=80)
                items_tree.column("subtotal", width=100)
                
                items_tree.pack(fill="both", expand=True)
                
                # 添加菜品数据
                for item in order_data["items"]:
                    items_tree.insert("", "end", values=(
                        item["name"],
                        f"¥{item['price']}",
                        item["quantity"],
                        f"¥{item['subtotal']:.2f}"
                    ))
                
                # 显示总价
                total_frame = tk.Frame(details_window, padx=10, pady=10)
                total_frame.pack(fill="x")
                
                tk.Label(total_frame, text=f"总计: ¥{order_data['total']:.2f}", font=("Arial", 12, "bold")).pack(side="right")
                
            else:
                messagebox.showerror("错误", "找不到订单详情")
                
        except Exception as e:
            messagebox.showerror("错误", f"查看订单详情失败: {str(e)}")
    
    def cancel_order(self):
        selected_item = self.orders_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择一个订单")
            return
        
        order_values = self.orders_tree.item(selected_item, "values")
        order_id = order_values[0]
        status = order_values[4]
        
        # 只允许取消"待处理"状态的订单
        if status != "待处理":
            messagebox.showinfo("提示", "只能取消待处理状态的订单")
            return
        
        if messagebox.askyesno("确认", f"确定要取消订单 #{order_id} 吗?"):
            try:
                # 读取订单数据
                with open("orders.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # 更新订单状态
                for order in data["orders"]:
                    if str(order["order_id"]) == order_id:
                        order["status"] = "已取消"
                        break
                
                # 保存更新后的订单数据
                with open("orders.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                
                messagebox.showinfo("成功", f"订单 #{order_id} 已取消")
                
                # 刷新订单列表
                self.load_user_orders()
                
            except Exception as e:
                messagebox.showerror("错误", f"取消订单失败: {str(e)}")
    
    def show_admin_panel(self):
        self.clear_window()
        
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)
        
        # 顶部标题栏
        title_frame = tk.Frame(main_frame, bg="#f0f0f0", height=50)
        title_frame.pack(fill="x")
        
        tk.Label(title_frame, text=f"管理员面板 - {self.current_admin}", font=("Arial", 14), bg="#f0f0f0").pack(side="left", padx=20, pady=10)
        tk.Button(title_frame, text="退出登录", command=self.show_login_frame).pack(side="right", padx=20, pady=10)
        
        # 主内容区 - 选项卡
        tab_control = ttk.Notebook(main_frame)
        
        # 用户管理选项卡
        user_tab = ttk.Frame(tab_control)
        tab_control.add(user_tab, text="用户管理")
        
        # 菜单管理选项卡
        menu_tab = ttk.Frame(tab_control)
        tab_control.add(menu_tab, text="菜单管理")
        
        # 订单管理选项卡
        order_tab = ttk.Frame(tab_control)
        tab_control.add(order_tab, text="订单管理")
        
        tab_control.pack(expand=1, fill="both", padx=10, pady=10)
        
        # 用户管理内容
        self.setup_user_management(user_tab)
        
        # 菜单管理内容
        self.setup_menu_management(menu_tab)
        
        # 订单管理内容
        self.setup_order_management(order_tab)
    
    def setup_user_management(self, parent_frame):
        # 创建用户表格
        columns = ("username", "phone")
        self.users_tree = ttk.Treeview(parent_frame, columns=columns, show="headings")
        
        self.users_tree.heading("username", text="用户名")
        self.users_tree.heading("phone", text="手机号码")
        
        self.users_tree.column("username", width=150)
        self.users_tree.column("phone", width=150)
        
        self.users_tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # 加载用户数据
        self.load_users_data()
        
        # 添加控制按钮
        control_frame = tk.Frame(parent_frame)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Button(control_frame, text="修改用户", command=self.edit_user).pack(side="left", padx=5)
        tk.Button(control_frame, text="删除用户", command=self.delete_user).pack(side="left", padx=5)
        tk.Button(control_frame, text="刷新", command=self.load_users_data).pack(side="left", padx=5)
    
    def load_users_data(self):
        try:
            with open("users.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 清除现有数据
            for item in self.users_tree.get_children():
                self.users_tree.delete(item)
            
            # 添加用户数据
            for user in data["users"]:
                self.users_tree.insert("", "end", values=(user["username"], user["phone"]))
            
        except Exception as e:
            messagebox.showerror("错误", f"加载用户数据失败: {str(e)}")
    
    def edit_user(self):
        selected_item = self.users_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择一个用户")
            return
        
        username = self.users_tree.item(selected_item, "values")[0]
        
        # 读取用户数据
        with open("users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        user_data = None
        for user in data["users"]:
            if user["username"] == username:
                user_data = user
                break
        
        if not user_data:
            messagebox.showerror("错误", "找不到用户数据")
            return
        
        # 创建编辑对话框
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"编辑用户 - {username}")
        edit_window.geometry("300x200")
        
        tk.Label(edit_window, text="用户名:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
        username_var = tk.StringVar(value=user_data["username"])
        username_entry = tk.Entry(edit_window, textvariable=username_var, state="readonly")
        username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(edit_window, text="手机号码:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        phone_var = tk.StringVar(value=user_data["phone"])
        phone_entry = tk.Entry(edit_window, textvariable=phone_var)
        phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(edit_window, text="密码:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        password_var = tk.StringVar(value=user_data["password"])
        password_entry = tk.Entry(edit_window, textvariable=password_var, show="*")
        password_entry.grid(row=2, column=1, padx=10, pady=5)
        
        def save_user():
            # 更新用户数据
            with open("users.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            for user in data["users"]:
                if user["username"] == username:
                    user["phone"] = phone_var.get()
                    user["password"] = password_var.get()
                    break
            
            with open("users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            messagebox.showinfo("成功", "用户信息已更新")
            edit_window.destroy()
            self.load_users_data()
        
        tk.Button(edit_window, text="保存", command=save_user).grid(row=3, column=0, columnspan=2, pady=10)
    
    def delete_user(self):
        selected_item = self.users_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择一个用户")
            return
        
        username = self.users_tree.item(selected_item, "values")[0]
        
        if messagebox.askyesno("确认", f"确定要删除用户 {username} 吗?"):
            # 读取用户数据
            with open("users.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 过滤掉要删除的用户
            data["users"] = [user for user in data["users"] if user["username"] != username]
            
            with open("users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            messagebox.showinfo("成功", f"用户 {username} 已删除")
            self.load_users_data()
    
    def setup_menu_management(self, parent_frame):
        # 创建菜单表格
        columns = ("id", "name", "price", "description")
        self.admin_menu_tree = ttk.Treeview(parent_frame, columns=columns, show="headings")
        
        self.admin_menu_tree.heading("id", text="ID")
        self.admin_menu_tree.heading("name", text="菜品名称")
        self.admin_menu_tree.heading("price", text="价格")
        self.admin_menu_tree.heading("description", text="描述")
        
        self.admin_menu_tree.column("id", width=50)
        self.admin_menu_tree.column("name", width=150)
        self.admin_menu_tree.column("price", width=80)
        self.admin_menu_tree.column("description", width=300)
        
        self.admin_menu_tree.pack(fill="both", expand=True)
        
        # 加载菜单数据
        self.load_admin_menu_data()
        
        # 添加控制按钮
        control_frame = tk.Frame(parent_frame)
        control_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Button(control_frame, text="添加新菜品", command=self.show_add_menu_item).pack(side="left", padx=5)
        tk.Button(control_frame, text="修改菜品", command=self.show_edit_menu_item).pack(side="left", padx=5)
        tk.Button(control_frame, text="删除菜品", command=self.delete_menu_item).pack(side="left", padx=5)
        tk.Button(control_frame, text="刷新", command=self.load_admin_menu_data).pack(side="left", padx=5)
    
    def load_admin_menu_data(self):
        try:
            with open("menu.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 清除现有数据
            for item in self.admin_menu_tree.get_children():
                self.admin_menu_tree.delete(item)
            
            # 添加新数据
            for idx, item in enumerate(data["items"]):
                self.admin_menu_tree.insert("", "end", values=(
                    idx+1, 
                    item["name"], 
                    f"¥{item['price']}", 
                    item["description"]
                ))
        except Exception as e:
            messagebox.showerror("错误", f"加载管理员菜单失败: {str(e)}")
    
    def show_add_menu_item(self):
        # 创建一个新窗口而不是清除主窗口
        add_window = tk.Toplevel(self.root)
        add_window.title("添加新菜品")
        add_window.geometry("300x200")
        
        frame = tk.Frame(add_window, padx=20, pady=20)
        frame.pack(expand=True)
        
        tk.Label(frame, text="添加新菜品", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame, text="菜品名称:").grid(row=1, column=0, sticky="e", pady=5)
        new_item_name = tk.Entry(frame, width=25)
        new_item_name.grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="价格:").grid(row=2, column=0, sticky="e", pady=5)
        new_item_price = tk.Entry(frame, width=25)
        new_item_price.grid(row=2, column=1, pady=5)
        
        tk.Label(frame, text="描述:").grid(row=3, column=0, sticky="e", pady=5)
        new_item_description = tk.Entry(frame, width=25)
        new_item_description.grid(row=3, column=1, pady=5)
        
        def add_item_callback():
            name = new_item_name.get()
            price_str = new_item_price.get()
            description = new_item_description.get()
            
            if not (name and price_str and description):
                messagebox.showerror("错误", "所有字段都必须填写")
                return
            
            try:
                price = float(price_str)
            except ValueError:
                messagebox.showerror("错误", "价格必须是数字")
                return
            
            with open("menu.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 检查菜品是否已存在
            for item in data["items"]:
                if item["name"] == name:
                    messagebox.showerror("错误", "菜品已存在")
                    return
            
            # 添加新菜品
            data["items"].append({
                "name": name,
                "price": price,
                "description": description
            })
            
            with open("menu.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            messagebox.showinfo("成功", "新菜品已添加")
            add_window.destroy()
            self.load_admin_menu_data()  # 刷新菜单数据
        
        tk.Button(frame, text="添加", command=add_item_callback).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="返回", command=add_window.destroy).grid(row=4, column=1, pady=10)
    
    def show_edit_menu_item(self):
        selected_item = self.admin_menu_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择一个菜品")
            return
        
        item_data = self.admin_menu_tree.item(selected_item, "values")
        item_id = int(item_data[0]) - 1  # 转换为索引（ID显示为从1开始，但索引从0开始）
        name = item_data[1]
        price = item_data[2].replace("¥", "")
        description = item_data[3]
        
        # 创建一个新窗口而不是清除主窗口
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"编辑菜品 - {name}")
        edit_window.geometry("300x200")
        
        frame = tk.Frame(edit_window, padx=20, pady=20)
        frame.pack(expand=True)
        
        tk.Label(frame, text="编辑菜品", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(frame, text="菜品名称:").grid(row=1, column=0, sticky="e", pady=5)
        edit_name_var = tk.StringVar(value=name)
        edit_name_entry = tk.Entry(frame, width=25, textvariable=edit_name_var)
        edit_name_entry.grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="价格:").grid(row=2, column=0, sticky="e", pady=5)
        edit_price_var = tk.StringVar(value=price)
        edit_price_entry = tk.Entry(frame, width=25, textvariable=edit_price_var)
        edit_price_entry.grid(row=2, column=1, pady=5)
        
        tk.Label(frame, text="描述:").grid(row=3, column=0, sticky="e", pady=5)
        edit_desc_var = tk.StringVar(value=description)
        edit_desc_entry = tk.Entry(frame, width=25, textvariable=edit_desc_var)
        edit_desc_entry.grid(row=3, column=1, pady=5)
        
        def save_item_callback():
            try:
                new_name = edit_name_var.get()
                new_price_str = edit_price_var.get()
                new_description = edit_desc_var.get()
                
                if not (new_name and new_price_str and new_description):
                    messagebox.showerror("错误", "所有字段都必须填写")
                    return
                    
                try:
                    new_price = float(new_price_str)
                except ValueError:
                    messagebox.showerror("错误", "价格必须是数字")
                    return
                    
                with open("menu.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                if 0 <= item_id < len(data["items"]):
                    # 更新菜品数据
                    data["items"][item_id]["name"] = new_name
                    data["items"][item_id]["price"] = new_price
                    data["items"][item_id]["description"] = new_description
                    
                    with open("menu.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    
                    messagebox.showinfo("成功", "菜品信息已更新")
                    edit_window.destroy()
                    self.load_admin_menu_data()  # 刷新菜单数据
                else:
                    messagebox.showerror("错误", "菜品索引无效")
            except Exception as e:
                messagebox.showerror("错误", f"保存菜品失败: {str(e)}")
        
        tk.Button(frame, text="保存", command=save_item_callback).grid(row=4, column=0, pady=10)
        tk.Button(frame, text="返回", command=edit_window.destroy).grid(row=4, column=1, pady=10)
    
    def delete_menu_item(self):
        selected_item = self.admin_menu_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择一个菜品")
            return
        
        item_data = self.admin_menu_tree.item(selected_item, "values")
        item_id = int(item_data[0]) - 1  # 转换为索引（ID显示为从1开始，但索引从0开始）
        name = item_data[1]
        
        if messagebox.askyesno("确认", f"确定要删除菜品 {name} 吗?"):
            try:
                with open("menu.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                if 0 <= item_id < len(data["items"]):
                    # 删除指定索引的菜品
                    del data["items"][item_id]
                    
                    with open("menu.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    
                    messagebox.showinfo("成功", f"菜品 {name} 已删除")
                    self.load_admin_menu_data()  # 刷新菜单数据
                else:
                    messagebox.showerror("错误", "菜品索引无效")
            except Exception as e:
                messagebox.showerror("错误", f"删除菜品失败: {str(e)}")
    
    def setup_order_management(self, parent_frame):
        # 创建订单表格
        columns = ("order_id", "username", "time", "items", "total", "status")
        self.admin_orders_tree = ttk.Treeview(parent_frame, columns=columns, show="headings")
        
        self.admin_orders_tree.heading("order_id", text="订单号")
        self.admin_orders_tree.heading("username", text="用户名")
        self.admin_orders_tree.heading("time", text="下单时间")
        self.admin_orders_tree.heading("items", text="菜品")
        self.admin_orders_tree.heading("total", text="总计")
        self.admin_orders_tree.heading("status", text="状态")
        
        self.admin_orders_tree.column("order_id", width=60)
        self.admin_orders_tree.column("username", width=100)
        self.admin_orders_tree.column("time", width=130)
        self.admin_orders_tree.column("items", width=250)
        self.admin_orders_tree.column("total", width=80)
        self.admin_orders_tree.column("status", width=80)
        
        self.admin_orders_tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # 加载订单数据
        self.load_all_orders()
        
        # 添加控制按钮
        control_frame = tk.Frame(parent_frame)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Button(control_frame, text="查看订单详情", command=self.admin_view_order_details).pack(side="left", padx=5)
        tk.Button(control_frame, text="更新订单状态", command=self.update_order_status).pack(side="left", padx=5)
        tk.Button(control_frame, text="刷新", command=self.load_all_orders).pack(side="left", padx=5)

    def load_all_orders(self):
        try:
            with open("orders.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 清除现有数据
            for item in self.admin_orders_tree.get_children():
                self.admin_orders_tree.delete(item)
            
            # 添加所有订单
            for order in data["orders"]:
                # 生成菜品简要信息
                items_summary = ", ".join([f"{item['name']} x{item['quantity']}" for item in order["items"]])
                if len(items_summary) > 30:
                    items_summary = items_summary[:27] + "..."
                
                self.admin_orders_tree.insert("", "end", values=(
                    order["order_id"],
                    order["username"],
                    order["order_time"],
                    items_summary,
                    f"¥{order['total']:.2f}",
                    order["status"]
                ))
        except Exception as e:
            messagebox.showerror("错误", f"加载订单失败: {str(e)}")

    def admin_view_order_details(self):
        selected_item = self.admin_orders_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择一个订单")
            return
        
        order_id = self.admin_orders_tree.item(selected_item, "values")[0]
        
        try:
            # 查找订单详情
            with open("orders.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            
            order_data = None
            for order in data["orders"]:
                if str(order["order_id"]) == order_id:
                    order_data = order
                    break
            
            if order_data:
                # 创建订单详情窗口
                details_window = tk.Toplevel(self.root)
                details_window.title(f"订单 #{order_id} 详情")
                details_window.geometry("500x400")
                
                # 订单信息
                info_frame = tk.Frame(details_window, padx=10, pady=10)
                info_frame.pack(fill="x")
                
                tk.Label(info_frame, text=f"订单号: {order_id}", font=("Arial", 12)).pack(anchor="w")
                tk.Label(info_frame, text=f"用户名: {order_data['username']}", font=("Arial", 12)).pack(anchor="w")
                tk.Label(info_frame, text=f"下单时间: {order_data['order_time']}", font=("Arial", 12)).pack(anchor="w")
                tk.Label(info_frame, text=f"状态: {order_data['status']}", font=("Arial", 12)).pack(anchor="w")
                
                # 菜品详情表格
                items_frame = tk.Frame(details_window, padx=10)
                items_frame.pack(fill="both", expand=True)
                
                columns = ("name", "price", "quantity", "subtotal")
                items_tree = ttk.Treeview(items_frame, columns=columns, show="headings")
                
                items_tree.heading("name", text="菜品名称")
                items_tree.heading("price", text="单价")
                items_tree.heading("quantity", text="数量")
                items_tree.heading("subtotal", text="小计")
                
                items_tree.column("name", width=150)
                items_tree.column("price", width=80)
                items_tree.column("quantity", width=80)
                items_tree.column("subtotal", width=100)
                
                items_tree.pack(fill="both", expand=True)
                
                # 添加菜品数据
                for item in order_data["items"]:
                    items_tree.insert("", "end", values=(
                        item["name"],
                        f"¥{item['price']}",
                        item["quantity"],
                        f"¥{item['subtotal']:.2f}"
                    ))
                
                # 显示总价
                total_frame = tk.Frame(details_window, padx=10, pady=10)
                total_frame.pack(fill="x")
                
                tk.Label(total_frame, text=f"总计: ¥{order_data['total']:.2f}", font=("Arial", 12, "bold")).pack(side="right")
                
            else:
                messagebox.showerror("错误", "找不到订单详情")
                
        except Exception as e:
            messagebox.showerror("错误", f"查看订单详情失败: {str(e)}")

    def update_order_status(self):
        selected_item = self.admin_orders_tree.focus()
        if not selected_item:
            messagebox.showinfo("提示", "请先选择一个订单")
            return
        
        values = self.admin_orders_tree.item(selected_item, "values")
        order_id = values[0]
        current_status = values[5]
        
        # 创建状态更新对话框
        status_window = tk.Toplevel(self.root)
        status_window.title(f"更新订单 #{order_id} 状态")
        status_window.geometry("300x150")
        
        frame = tk.Frame(status_window, padx=20, pady=20)
        frame.pack(expand=True)
        
        tk.Label(frame, text=f"当前状态: {current_status}").grid(row=0, column=0, columnspan=2, pady=5)
        
        tk.Label(frame, text="新状态:").grid(row=1, column=0, sticky="e", pady=5)
        status_var = tk.StringVar(value=current_status)
        status_combo = ttk.Combobox(frame, textvariable=status_var, values=["待处理", "已完成", "已取消"])
        status_combo.grid(row=1, column=1, pady=5)
        
        def save_status():
            new_status = status_var.get()
            
            if new_status == current_status:
                status_window.destroy()
                return
            
            try:
                # 读取订单数据
                with open("orders.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # 更新订单状态
                for order in data["orders"]:
                    if str(order["order_id"]) == order_id:
                        order["status"] = new_status
                        break
                
                # 保存更新后的订单数据
                with open("orders.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                
                messagebox.showinfo("成功", f"订单 #{order_id} 状态已更新为 {new_status}")
                status_window.destroy()
                
                # 刷新订单列表
                self.load_all_orders()
                
            except Exception as e:
                messagebox.showerror("错误", f"更新订单状态失败: {str(e)}")
        
        tk.Button(frame, text="保存", command=save_status).grid(row=2, column=0, pady=10)
        tk.Button(frame, text="取消", command=status_window.destroy).grid(row=2, column=1, pady=10)

# 创建主程序
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantSystem(root)
    root.mainloop() 