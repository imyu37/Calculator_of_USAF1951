import FreeSimpleGUI as sg

# USAF 1951分辨率测试靶标准
# 空间频率公式: f = 2^(group + (element-1)/6) [lp/mm]
# 线宽公式: line_width = 1/(2*f) [mm]

# 界面主题设置
sg.theme("LightGrey1")

# USAF 1951组和元素范围
USAF_GROUPS = list(range(-2, 10))  # 组: -2 到 9
USAF_ELEMENTS = list(range(1, 7))  # 元素: 1 到 6


def calculate_spatial_frequency(group, element):
    """
    计算USAF 1951的空间频率

    参数:
    group: 组号 (-2到7)
    element: 元素号 (1到6)

    返回:
    空间频率 (lp/mm)
    """
    return 2 ** (group + (element - 1) / 6)


def calculate_line_width(spatial_frequency_lpmm, unit="mm"):
    """
    计算线宽

    参数:
    spatial_frequency_lpmm: 空间频率 (lp/mm)
    unit: 单位 ('mm', 'μm', 'nm')

    返回:
    线宽 (指定单位)
    """
    line_width_mm = 1 / (2 * spatial_frequency_lpmm)

    if unit == "mm":
        return line_width_mm
    elif unit == "μm":
        return line_width_mm * 1000
    elif unit == "nm":
        return line_width_mm * 1e6
    else:
        return line_width_mm


def get_usaf_description(group, element):
    """获取USAF 1951模式的描述"""
    descriptions = {
        -2: "极低分辨率模式",
        -1: "低分辨率模式",
        0: "中等分辨率模式",
        1: "标准分辨率模式",
        2: "高分辨率模式",
        3: "超高分辨率模式",
        4: "极高高分辨率模式",
        5: "专业级分辨率模式",
        6: "科研级分辨率模式",
        7: "极限分辨率模式",
    }
    return descriptions.get(group, "未知分辨率模式")


# 输入参数布局
input_layout = [
    [
        sg.Text(
            "USAF 1951 参数设置",
            font=("微软雅黑", 12),
            expand_x=True,
            justification="center",
        )
    ],
    [
        sg.Column(
            [
                [
                    sg.T("组 (Group)", size=12),
                    sg.Combo(USAF_GROUPS, default_value=0, key="-GROUP-", size=15),
                ],
                [
                    sg.T("元素 (Element)", size=12),
                    sg.Combo(USAF_ELEMENTS, default_value=1, key="-ELEMENT-", size=15),
                ],
                [
                    sg.T("单位选择", size=12),
                    sg.Combo(
                        ["毫米 (mm)", "微米 (μm)", "纳米 (nm)"],
                        default_value="毫米 (mm)",
                        key="-UNIT-",
                        size=15,
                    ),
                ],
            ],
            pad=(0, 10),
        )
    ],
]

# 结果展示布局
result_layout = [
    [sg.Text("计算结果", font=("微软雅黑", 11), text_color="#2B579A")],
    [
        sg.Multiline(
            "",
            key="-RESULT-",
            size=(80, 10),
            font=("微软雅黑", 9),
            background_color="#F5F5F5",
            text_color="#C7501A",
            disabled=True,
        )
    ],
]

# 参考信息布局
reference_layout = [
    [sg.Text("USAF 1951 参考信息", font=("微软雅黑", 11), text_color="#2B579A")],
    [
        sg.Multiline(
            "",
            key="-REFERENCE-",
            size=(80, 8),
            font=("Consolas", 10),
            background_color="#F0F0F0",
            text_color="#2B579A",
            disabled=True,
        )
    ],
]

# 界面布局
layout = [
    input_layout,
    result_layout,
    reference_layout,
    [
        sg.Button(
            "计算", size=12, button_color=("white", "#4B8BBE"), bind_return_key=True
        ),
        sg.Button("显示全部模式", size=15, button_color=("white", "#32CD32")),
        sg.Button("清除", size=10, button_color=("white", "#6D6D6D")),
        sg.Button("退出", size=10, button_color=("white", "#8B0000")),
    ],
]

# 创建窗口
window = sg.Window("", layout, font=("微软雅黑", 10), finalize=True)
window.size = (550, 600)


def format_result(group, element, spatial_frequency, line_width, unit):
    """格式化结果显示"""
    unit_map = {"毫米 (mm)": "mm", "微米 (μm)": "μm", "纳米 (nm)": "nm"}
    unit_short = unit_map.get(unit, "mm")

    result_text = "USAF 1951 计算结果:\n"
    result_text += "═════════════════════════════════════\n"
    result_text += f"组 (Group): {group}\n"
    result_text += f"元素 (Element): {element}\n"
    result_text += f"模式描述: {get_usaf_description(group, element)}\n\n"

    result_text += f"空间频率: {spatial_frequency:.1f} lp/mm\n\n"

    result_text += f"线宽 ({unit_short}):\n"
    if unit_short == "mm":
        result_text += f"  • {line_width:.6f} mm\n"
        result_text += f"  • {line_width * 1000:.2f} μm\n"
        result_text += f"  • {line_width * 1e6:.1f} nm\n"
    elif unit_short == "μm":
        result_text += f"  • {line_width / 1000:.6f} mm\n"
        result_text += f"  • {line_width:.2f} μm\n"
        result_text += f"  • {line_width * 1000:.1f} nm\n"
    else:  # nm
        result_text += f"  • {line_width / 1e6:.6f} mm\n"
        result_text += f"  • {line_width / 1000:.2f} μm\n"
        result_text += f"  • {line_width:.1f} nm\n"

    result_text += "\n物理意义:\n"
    if spatial_frequency < 1:
        result_text += "  • 适用于宏观光学系统检测\n"
        result_text += "  • 大型光学元件分辨率测试\n"
    elif spatial_frequency < 10:
        result_text += "  • 适用于一般光学镜头测试\n"
        result_text += "  • 相机镜头分辨率评估\n"
    elif spatial_frequency < 100:
        result_text += "  • 适用于精密光学系统\n"
        result_text += "  • 显微镜物镜分辨率测试\n"
    else:
        result_text += "  • 适用于高分辨率光学系统\n"
        result_text += "  • 半导体检测设备校准\n"

    return result_text


def generate_reference_table():
    """生成USAF 1951参考表"""
    reference_text = "USAF 1951 标准分辨率表 (lp/mm):\n"
    reference_text += (
        "\nGroup│Element 1│Element 2│Element 3│Element 4│Element 5│Element 6\n"
    )
    reference_text += (
        "─────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────\n"
    )

    for group in USAF_GROUPS:
        reference_text += f"  {group:2} │"
        for element in USAF_ELEMENTS:
            freq = calculate_spatial_frequency(group, element)
            reference_text += f" {freq:8.2f}│"
        reference_text += "\n"

    reference_text += "\n常用应用场景:\n"
    reference_text += "• Group -2 to 0: 大型光学系统, 投影仪\n"
    reference_text += "• Group 1 to 3: 相机镜头, 望远镜\n"
    reference_text += "• Group 4 to 5: 显微镜, 精密仪器\n"
    reference_text += "• Group 6 to 7: 半导体检测, 科研设备\n"

    return reference_text


# 初始化参考信息
window["-REFERENCE-"].update(generate_reference_table())

# 事件循环
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "退出"):
        break

    if event == "计算":
        try:
            # 获取输入参数
            group = int(values["-GROUP-"])
            element = int(values["-ELEMENT-"])
            unit = values["-UNIT-"]

            # 计算空间频率和线宽
            spatial_frequency = calculate_spatial_frequency(group, element)
            unit_short = {"毫米 (mm)": "mm", "微米 (μm)": "μm", "纳米 (nm)": "nm"}[unit]
            line_width = calculate_line_width(spatial_frequency, unit_short)

            # 格式化并显示结果
            result_text = format_result(
                group, element, spatial_frequency, line_width, unit
            )
            window["-RESULT-"].update(result_text)

        except (ValueError, TypeError):
            sg.popup_error("输入错误！请选择有效的组和元素值", title="错误提示")

    if event == "显示全部模式":
        reference_text = generate_reference_table()
        window["-REFERENCE-"].update(reference_text)
        sg.popup(
            reference_text,
            font=("consolas", 10),
            title="USAF 1951 参考表",
            non_blocking=True,
        )
    if event == "清除":
        window["-RESULT-"].update("")

window.close()
