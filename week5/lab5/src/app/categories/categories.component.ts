import { Component, OnInit } from '@angular/core';
import {Category} from '../category';
import {CategoriesService} from '../categories.service';
import { from } from 'rxjs';
@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})
export class CategoriesComponent implements OnInit {
  categories: Category[];
  constructor(private categoryService: CategoriesService) { }
  getCategories(): void{
    this.categoryService.getCategories().subscribe(categories=>this.categories=categories);
  }
  ngOnInit(): void {
    this.getCategories();
  }

}
