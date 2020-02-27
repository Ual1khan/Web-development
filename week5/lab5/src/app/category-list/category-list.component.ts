import { Component, OnInit, Input } from '@angular/core';
import { Category } from '../category';
import {products, Product} from '../products';

import { CategoriesService } from '../categories.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrls: ['./category-list.component.css']
})
export class CategoryListComponent implements OnInit {
  @Input() category:Category;
  products=products;
  constructor(private route: ActivatedRoute,
    private _categoriesService: CategoriesService,     
    private location: Location
  ) { }

  getCategory(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this._categoriesService.getCategory(id)
      .subscribe(category => this.category =category);
  }
  ngOnInit(): void {
    this.getCategory();
  }

  goBack(): void {
    this.location.back();
  }
}
