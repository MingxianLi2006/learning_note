% 定义你要检查的工具箱（左边是官方全名，右边是显示用的简称）
toolboxes = {
    'Signal Processing Toolbox',   'Signal processing toolbox';
    'Control System Toolbox',      'Control system toolbox';
    'Audio Toolbox',               'Audio toolbox';
    'Symbolic Math Toolbox',       'Symbolic Math Toolbox'
};

% 获取当前已安装的所有工具箱列表
v = ver;
installedNames = {v.Name};

% 逐个检查并输出结果
fprintf('===== 工具箱安装检查 =====\n');
for i = 1:size(toolboxes, 1)
    officialName = toolboxes{i, 1};
    displayName  = toolboxes{i, 2};
    
    if any(strcmpi(installedNames, officialName))
        fprintf('✔ 已安装: %s\n', displayName);
    else
        fprintf('✘ 未安装: %s\n', displayName);
    end
end