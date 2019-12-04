#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   battlePokemonPackage.py
@Time    :   2019/12/01 19:23:51
@Author  :   Jawa 
@Version :   1.0
@Contact :   840132699@qq.com
@Desc    :   将精灵初始信息和对战信息打包成一只对战精灵
'''


class BattlePokemon():
    '''对战精灵的生成'''

    def package_pkmon(self, num, level, name, type1,
                      type2, ability, hp, atk, defend,
                      atk_sp, defend_sp, speed, hp_v, atk_v,
                      defend_v, atk_sp_v, defend_sp_v, speed_v, moves):
        '''
        对战精灵添加
        攻击、防御、速度、特攻、特防、命中率、闪避率
        七项能力等级提高或降低的状态

        '''
        # 能力等级初始值都为0
        atk_level = 0
        defend_level = 0
        atk_sp_level = 0
        defend_sp_level = 0
        speed_level = 0
        accuracy_level = 0
        avoid_level = 0
        base_info = {
            "num": num,
            "level": level,
            "name": name,
            "type1": type1,
            "type2": type2,
            "ability": ability,
            "hp_max": hp

        }
        statistic = {
            "hp": hp,
            "atk": atk,
            "defend": defend,
            "atk_sp": atk_sp,
            "defend_sp": defend_sp,
            "speed": speed
        }
        statistic_level = {
            "atk_level": atk_level,
            "defend_level": defend_level,
            "atk_sp_level": atk_sp_level,
            "defend_sp_level": defend_sp_level,
            "speed_level": speed_level,
            "accuracy_level": accuracy_level,
            "avoid_level": avoid_level
        }
        # 宝可梦基本信息
        individual = {
            "hp_v": hp_v,
            "atk_v": atk_v,
            "defend_v": defend_v,
            "atk_sp_v": atk_sp_v,
            "defend_sp_v": defend_sp_v,
            "speed_v": speed_v
        }

        pokemon = {
            "base_info": base_info,
            "statistic": statistic,
            "individual": individual,
            "statistic_level": statistic_level,
            "moves": moves
        }
        return pokemon
