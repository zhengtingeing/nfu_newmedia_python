from king_hero import get_hero_num,hero_information
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    output_prompt = '请输入你想要搜索的英雄'
    return render_template('entry.html',
                           the_output_prompt=output_prompt,
                           the_entry_title='王者荣耀英雄查询')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    hero_name = request.form['input_hero_name']
    results_title = '以下是您的结果'
    output_prompt_error = '请输入正确的英雄名'
    dict_all = hero_information(hero_name)
    if 'error' in dict_all:
        return render_template('entry.html',
                               the_entry_title='欢迎来到王者荣耀！',
                               the_output_prompt_error=output_prompt_error
                               )
    else:
        return render_template('results.html',
                               the_results_title=results_title,
                               the_name=hero_name,
                               output_skill_passive=dict_all[hero_name][1][0],
                               output_skill_1=dict_all[hero_name][1][1],
                               output_skill_2=dict_all[hero_name][1][2],
                               output_skill_3=dict_all[hero_name][1][3],
                               output_story=dict_all[hero_name][0]
                               )

if __name__ == '__main__':
    app.run(debug=True)
