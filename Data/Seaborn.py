import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


temperature = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
ice_cream_sales = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
sns.scatterplot(x = temperature, y = ice_cream_sales) # กรณีที่เป็น dataframe จะเป็น (x = 'column1', y = 'column2', data = df)
plt.show()

grades = ['A', 'B', 'C', 'D', 'F', 'A', 'C', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'C', 'D', 'A', 'B', 'A', 'F', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'B', 'B', 'C', 'A', 'B', 'A', 'C', 'C', 'B', 'B', 'D', 'F', 'B', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'A', 'B']
sns.countplot(y = grades)
plt.show()
sns.countplot(x = grades)
plt.show()
# or sns.histplot(x = 'Age', data = sleep, hue = 'Gender', alpha = 0.5, multiple = 'stack')

Age_BP = {'Age': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
        'Blood Pressure': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
        'Gender': ['M', 'F', 'F', 'M', 'F', 'F', 'M', 'M', 'F', 'M'],
        'DM' : ['True', 'False', 'False', 'True', 'False', 'False', 'True', 'False', 'True', 'False'],
        'BMI': [22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
        }
Age_BP = pd.DataFrame(Age_BP)
hue_colors = {'M':'Navy', 'F':'Pink'}
sns.scatterplot(x = 'Age', y = 'Blood Pressure', data = Age_BP, hue = 'Gender', palette = hue_colors, style = 'Gender')
sns.relplot(x = 'Age', y = 'Blood Pressure', kind = 'scatter', data = Age_BP, hue = 'Gender', style = 'Gender', size = 'BMI')
plt.show()
 
#sns.relplot จะช่วยแยกแต่ละ hue ออกมาเป็น subplot
sns.relplot(x = 'Age', y = 'Blood Pressure', kind = 'scatter', data = Age_BP, col = 'Gender', row = 'DM') # สามารถใช้ argument row หรือ col อย่างใดอย่างหนึ่งก็ได้
plt.show()


data = {'Gender': ['M', 'F', 'F', 'M', 'M', 'F', 'M', 'F', 'F', 'M',
                  'F', 'M', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'],
        'Smoker': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No',
                  'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No']}
Sex_Smoke = pd.DataFrame(data)
sns.countplot(x = 'Smoker', data = Sex_Smoke, hue = 'Gender', hue_order=['F', 'M']) 
plt.show()

# sns.catplot(x = 'columns that are categorical variables', data = df, kind = 'count', order = ['', '',...])
# sns.catplot(x = 'columns that are categorical variables', y = 'columns that are continuous variables', data = df, kind = 'bar', order = ['','',...])
        # the bar plot will shows 95% CI line
# sns.catplot(x = 'columns that are categorical variables', y = 'columns that are continuous variables', data = df, kind = 'point', capsize = 0.2, order = ['','',...])
        # point plot จะเหมือน barplot แต่อ่านง่ายกว่า มีการแสดงเส้นของ 95% CI เหมือนกัน, ถ้าอยากปิด ci -> ci = False
        # ถ้าหากอยากลบเส้นเชื่อม join = False
        # dodge = True : set ให้แต่ละ hue ของ pointplot ไม่เหลื่อมกัน
        # ค่ากลาง default คือ mean ถ้าอยากเปลี่ยนเป้น median - > estimator = median
# sns.catplot() สามารถแยกเป็น subplot โดยใส่ argument row = '', col = '' เช่นเดียวกับ .relplot()
# sns.catplot(x = 'columns that are categorical variables', y = 'columns that are continuous variables', data = df, kind = 'box', sym = '', whis = [0, 100], order = ['','',...])
        # สามารถแยก subplot ด้วย argument hue = 'column' ได้เหมือนกัน
# sns.set_style()
# sns.set_palette()
# sns.set_context() : 'paper', 'notebook', 'talk', 'poster'
# ax = sns.catplot()
        # ax.fig.suptitle('') : ชื่อ Main title 
        # ax.set_titles ('{column_name}') : ในกรณีที่มี row = '', col = '' argument เพื่อแยก subplot , หรือกรณีที่ไม่ใช้ relplot() หรือ catplot()
        # ax.set(xlabel = '', ylabel = '')
# plt.xticks(rotation = 90)
# sns.heatmap(df.corr(), annot = True)
# sns.pairplot(data = df, vars = ['', '', ''], hue = '', palette = '', plot_kws = {'alpha':0.5}) : vars คือ columns ของตัวแปรที่สนใจ
# sns.histplot(data = df, x = '', hue = '', bins = )
        # sns.kdeplot(data = df, x = '', hue = '', bins = , cut = ) : จะดูง่ายกว่ากรณีมีหลาย plot ซ้อนทับกัน, cut เป็น argument เสริม ที่บอกว่าแกน X จะให้เริ่มต้นที่ค่าไหน
                # cumulative = True : เปลี่ยนจากกราฟการกระจาย เป็นกราฟ cumulative


# intermediate seaborn 
# style
        # sns.set(font_scale = 1.0)
        # sns.set_style(['white', 'dark', 'whitegrid', 'darkgrid', 'ticks'])
        # sns.despine(left = True) : remove y axis of left side
# custom palettes 
        # display color palettes : sns.palplot(sns.color_palette('Purple', 8))
        # Sequential colors : sns.color_palette('Blues', 12) 
        # Diverging colors : sns.color_palette('BrBG', 12) 
        # reverse colors : sns.color_palette('BrBG', 12)[::-1]
# one variable : distribution plot     
        # sns.displot(data = df, x = '', kind = 'hist', kde = True, fill = True, bins = , alpha = 0.5) : แสดงทั้ง histogram & kde plot
# two variables : regression plot
        # sns.lmplot(data = df, x = '', y = '', ci = 95, hue = '', col = '', row = '', col_order = ['', '',...], scatter_kws = {'alpha' : 0.5}, line_kws = {'color' : 'orange'})

# custom seaborn with matplotlib
        # fig, (ax0, ax1) = plt.subplots(nrows = 1, ncols =2, sharey = True) : sharey =  all subplots will share the same y-axis scale
        # sns.histplot(ax = ax0)
        # sns.histplot(ax = ax1)
        # ax1.set(xlabel = '', xlim = (0, 10000))
        # ax1.axvline(x = 5000, label = '', linestyle = '--', color = '')
        # ax1.legend

# categorical plot types : either x or y axis may be categorical variables
        # show each individual observations : stripplot / swarmplot
        # show abstract representations : boxplot / violinplot / boxenplot
        # statistical estimates : barplot / pointplot / countplot
        # matrix plot : 
                # table = pd.crosstab(df['cat1'], df['cat2'], values = df['continuous variables']. aggfunc = 'mean').round(0)
                # sns.heatmap(table, annot = True, fmt = 'd', cmap = 'YlGnBu', cbar = False, linewidths = .5)
                        # cmap = color palette, cbar = color bar, fmt = display value in cells as integer
                # sns.heatmap(df[['', '', '', '']].corr(), cmap = 'YlGnBu')
                        # plt.xticks(rotation = 90)

# regression plot       
        # sns.regplot(data = , x = '', y = '') : order = 2 กรณีเป็น polynomial regression model
                # x_bins = แบ่งกลุ่มในข้อมูลเป็น bins โดย estimator เป็น mean 
        # sns.residplot(data = , x = '', y = '') : order = 2 กรณีเป็น polynomial regression model
                # horizontal line at y=0 to indicate the ideal case where the predicted values match the observed values perfectly
                # useful for assessing the goodness-of-fit of a linear regression model and detecting potential violations of its assumptions

# joint grid : plot 2 plot ลงบนภาพเดียว โดยจะมี scatterplot & histogram ontop
        # g = sns.JointGrid(data = df, x = '', y ='') : X & Y เป็น continuous variables
        # g.plot(sns.regplot, sns.histplot) or more advanced
                # g.plot_joint(sns.kdeplot)
                # g.plot_marginals(sns.kdeplot, shade = True)
# joint plot : more easier than joint grid
        # sns.jointplot(data =df, x = '', y = '', kind = 'hex/scatter/reg/resid/kde') 
                # ถ้า kind = 'reg/resid' ควรใส่ argument order = 2 ถ้าหากหาความสัมพันธ์แบบ polynomial regression
        # example :
                # g = (sns.jointplot(data =df, x = '', y = '', kind = 'scatter').plot_joint(sns.kdeplot))